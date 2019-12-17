######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
import json

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage

######################################
# 系统模块
######################################
import datetime

######################################
# 自建模块
######################################
from utils.login_check import LoginStatusCheck
from .forms import *
from .models import *
from operation_record.models import UserOperationRecord
from utils.send_email import send_email_verificode
from utils.user_func import get_ip_location
from oms.settings import GAODE_API_KEY, CITY_ID, DEVELPER_EMAIL_ADDRESS, EMAIL_HOST_USER
# from online_management.models import TroubleRecord, DeployRecord
from utils.code_response import responseFomat

def UserOperation(op_user,belong,status,op_num,operation,action):
    try:
        op_record = UserOperationRecord()
        op_record.op_user = op_user
        op_record.belong = belong
        op_record.status = status
        op_record.op_num = op_num
        op_record.operation = operation
        op_record.action = action
        op_record.save()
        return 0
    except Exception as e:
        return e


######################################
# 首页
######################################
class IndexView(LoginStatusCheck, View):
    def get(self, request):
        # 获取年月列表
        ym_list = []
        # tr_list = []
        # dep_list = []
        y_now = datetime.datetime.now().year
        m_now = datetime.datetime.now().month
        i = 0
        while (i < 12):
            ym_list.append(str(y_now) + '-' + str(m_now))
            # tr_list.append(TroubleRecord.objects.filter(event_time__year=y_now, event_time__month=m_now).count())
            # dep_list.append(DeployRecord.objects.filter(deploy_time__year=y_now, deploy_time__month=m_now).count())

            m_now = m_now - 1
            if m_now == 0:
                m_now = 12
                y_now = y_now - 1

            i += 1

        # tr_list = list(reversed(tr_list))
        ym_list = list(reversed(ym_list))
        # dep_list = list(reversed(dep_list))

        return render(request, 'users/index.html', context=context)

######################################
# 登录
######################################
class LoginView(View):
    def post(self, request):
        # user_login_form = UerLoginForm(request.POST)

        # 输入合法
        # if user_login_form.is_valid():
            # 获取提交的登录信息
        data=json.loads(request.body)
        login_username = data.get('username')
        login_password = data.get('password')

        # 认证用户
        user = authenticate(username=login_username, password=login_password)

        # 判断用户是否正确
        if user is not None:
            if not user.is_active:
                return HttpResponseRedirect(reverse('users:send_active_email'))
            elif (user.status != 1):
                msg = '用户已停用，请联系管理员！'
                return responseFomat().dataHandleFailed()
            else:
                login(request, user)

                # 保存登录信息
                login_record = UserLoginInfo()
                login_record.action = 1
                login_record.user = user
                login_record.agent = request.META['HTTP_USER_AGENT']
                login_record.ip = request.META['REMOTE_ADDR']
                login_record.address = '中国 北京'
                # login_record.address = get_ip_location(request.META['REMOTE_ADDR'])
                login_record.save()

                # 添加操作记录
                UserOperation(op_user=user,
                              belong=3,
                              status=1,
                              op_num=user.id,
                              operation=5,
                              action="用户 [ %s ] 登录了系统" % user.user_name)

                return HttpResponseRedirect(reverse('users:index'))
        else:
            return responseFomat().dataHandleFailed()
        # else:
        #     return responseFomat().dataHandleFailed()


######################################
# 邮箱登录
######################################
class OtherLoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 增加邮箱验证
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

######################################
# 登出
######################################
class LogoutView(LoginStatusCheck, View):
    def get(self, request):
        # 保存登录信息
        login_record = UserLoginInfo()
        login_record.action = 2
        login_record.user = request.user
        login_record.agent = request.META['HTTP_USER_AGENT']
        login_record.ip = request.META['REMOTE_ADDR']
        # login_record.address = get_ip_location(request.META['REMOTE_ADDR'])
        login_record.address = '中国 北京'
        login_record.save()

        # 添加操作记录
        op_record = UserOperationRecord()
        op_record.op_user = request.user
        op_record.belong = 3
        op_record.status = 1
        op_record.op_num = request.user.id
        op_record.operation = 6
        op_record.action = "用户 [ %s ] 退出了系统" % request.user.user_name
        op_record.save()

        logout(request)

        return HttpResponseRedirect(reverse('users:login'))

######################################
# 忘记密码
######################################
class ForgetPasswordView(View):
    def get(self, request):
        context = {}
        return render(request, 'users/login/forget_password.html', context=context)

    def post(self, request):
        user_forget_password_form = UserForgetPasswordForm(request.POST)

        if user_forget_password_form.is_valid():
            email = request.POST.get('email')
            if UserProfile.objects.filter(email=email):
                # 发送邮件
                send_status = send_email_verificode(email, 'forget')
                if send_status:
                    msg = '邮件已发送，请注意查收！'
                else:
                    msg = '邮件发送失败，请检查！'
            else:
                msg = '该邮箱不存在，请检查！'
        else:
            msg = '邮箱格式不合法，请检查！'

        context = {
            'msg': msg,
        }
        return render(request, 'users/login/forget_password.html', context=context)

######################################
# 重置密码
######################################
class ResetPasswordView(View):
    def get(self, request, reset_code):
        code_record = UserEmailVirificationCode.objects.filter(code=reset_code).filter(purpose='forget').latest(
            'add_time')
        if code_record:
            if not code_record.is_use:
                if (datetime.datetime.now() - code_record.add_time).seconds > 300:
                    msg = '验证码已过期！'
                    context = {
                        'msg': msg,
                    }
                    return render(request, 'users/login/forget_password.html', context=context)
                else:
                    context = {
                        'reset_code': reset_code
                    }
                    return render(request, 'users/login/reset_password.html', context=context)
            else:
                msg = '验证码已被使用！'
                context = {
                    'msg': msg,
                }
                return render(request, 'users/login/forget_password.html', context=context)
        else:
            msg = '地址有误，请重新发送重置邮件！'
            context = {
                'msg': msg,
            }
            return render(request, 'users/login/forget_password.html', context=context)

######################################
# 重置修改密码
######################################
class ModifyPasswordView(View):
    def post(self, request):
        new_password = request.POST.get('new_password')
        renew_password = request.POST.get('renew_password')
        reset_code = request.POST.get('reset_code')
        if new_password != renew_password:
            msg = '密码不一致！'
            context = {
                'msg': msg,
                'reset_code': reset_code
            }
            return render(request, 'users/login/reset_password.html', context=context)
        elif (len(new_password) < 6) or (len(new_password) > 20):
            msg = '密码长度不符合要求！'
            context = {
                'msg': msg,
                'reset_code': reset_code
            }
            return render(request, 'users/login/reset_password.html', context=context)
        else:
            # 获取相应的用户
            code_record = UserEmailVirificationCode.objects.filter(code=reset_code).latest('add_time')
            email = code_record.email
            user = UserProfile.objects.get(email=email)

            # 修改密码
            try:
                user.password = make_password(new_password)
                user.save()

                # 修改验证码状态
                code_record.is_use = True
                code_record.save()

                msg = '密码重置成功！'
                context = {
                    'msg': msg,
                }
                return render(request, 'users/login/login.html', context=context)
            except Exception as e:
                msg = '密码重置失败，请重试！'
                context = {
                    'msg': msg,
                    'reset_code': reset_code
                }
                return render(request, 'users/login/reset_password.html', context=context)


######################################
# 用户头像
######################################
class UserAvatarView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'user_management'
        web_chose_left_2 = 'user_info'
        web_chose_middle = 'user_avatar'

        for_round = range(1, 11)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'for_round': for_round,
        }

        return render(request, 'users/user/user_change_avatar.html', context=context)


######################################
# 上传修改用户头像
######################################
class ChangeUserAvatarUploadView(LoginStatusCheck, View):
    def post(self, request):
        avatar_pic = request.FILES.get('img')
        if avatar_pic:
            user = request.user
            user.avatar = avatar_pic
            user.save()
            return HttpResponse('{"status":"success", "msg":"用户头像上传修改成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"falied", "msg":"用户头像上传修改失败！"}', content_type='application/json')

######################################
# 选择修改用户头像
######################################
class ChangeUserAvatarChoseView(LoginStatusCheck, View):
    def post(self, request):
        user = request.user
        new_avatar = request.POST.get('avatar')

        if new_avatar:
            user.avatar = new_avatar
            # 保存修改
            user.save()
            return HttpResponse('{"status":"success", "msg":"用户头像修改成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"falied", "msg":"用户头像修改失败！"}', content_type='application/json')

######################################
# 修改用户密码
######################################
class ChangeUserPasswordView(LoginStatusCheck, View):
    def post(self, request):
        change_user_password_form = ChangeUserPasswordForm(request.POST)
        if change_user_password_form.is_valid():
            cur_password = request.POST.get('cur_password')
            new_password = request.POST.get('new_password')
            renew_password = request.POST.get('renew_password')

            if new_password != renew_password:
                msg = '两次密码不一致！'
            elif authenticate(username=request.user.username, password=cur_password) is None:
                msg = '当前密码不正确！'
            else:
                request.user.password = make_password(new_password)
                request.user.save()
                return HttpResponseRedirect(reverse('users:login'))
        else:
            msg = '输入不合法，密码最小长度为 6 位！'

        context = {
            'msg': msg
        }
        return render(request, 'users/user/user_change_passwd.html', context=context)


######################################
# 用户登录信息
######################################
class UserLoginRecordView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'log_management'
        web_chose_left_2 = 'login_log'
        web_chose_middle = ''

        user_check = 'all'

        # 登录日志记录
        records = UserLoginInfo.objects.filter(user=request.user).order_by('-add_time')

        # 查询
        keyword = request.GET.get('keyword', '')

        if keyword != '':
            records = records.filter(
                Q(ip__icontains=keyword) | Q(agent__icontains=keyword) | Q(address__icontains=keyword)
            )

        if request.GET.get('user_check'):
            if request.GET.get('user_check') == 'login':
                records = records.filter(action=1)
                user_check = 'login'

            if request.GET.get('user_check') == 'logout':
                records = records.filter(action=2)
                user_check = 'logout'

        record_nums = records.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(records, 19, request=request)

        # 分页处理后的 QuerySet
        records = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'records': records,
            'record_nums': record_nums,
            'keyword': keyword,
            'user_check': user_check,
        }
        return render(request, 'users/user/user_login_record.html', context=context)


######################################
# 用户操作信息
######################################
class UserOperationRecordView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'log_management'
        web_chose_left_2 = 'user_log'
        web_chose_middle = ''

        # 日志记录
        records = UserOperationRecord.objects.filter(belong=2).order_by('-add_time')

        # 查询
        keyword = request.GET.get('keyword', '')

        if keyword != '':
            records = records.filter(Q(op_user__user_name__icontains=keyword) | Q(action__icontains=keyword))

        # 用户选择
        user_check = request.GET.get('user_check', 'all')

        # 添加
        if user_check == 'add':
            records = records.filter(operation=1)

        # 修改
        if user_check == 'edit':
            records = records.filter(operation=2)

        # 启用
        if user_check == 'up':
            records = records.filter(operation=3)

        # 停用
        if user_check == 'down':
            records = records.filter(operation=4)

        record_nums = records.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(records, 19, request=request)

        # 分页处理后的 QuerySet
        records = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'records': records,
            'record_nums': record_nums,
            'keyword': keyword,
            'user_check': user_check,
        }
        return render(request, 'users/user/user_op_record.html', context=context)



# 错误页面
def page_not_found(request):
    return render(request, 'error/404.html')


def page_error(request):
    return render(request, 'error/500.html')


def permission_denied(request):
    return render(request, 'error/403.html')


#
# ######################################
# # 用户邮箱
# ######################################
# class UserEmailView(LoginStatusCheck, View):
#     def get(self, request):
#         # 页面选择
#         web_chose_left_1 = 'user_management'
#         web_chose_left_2 = 'user_info'
#         web_chose_middle = 'user_email'
#
#         context = {
#             'web_chose_left_1': web_chose_left_1,
#             'web_chose_left_2': web_chose_left_2,
#             'web_chose_middle': web_chose_middle,
#         }
#         return render(request, 'users/user/user_change_email.html', context=context)
#
# ######################################
# # 发送修改用户邮箱验证码
# ######################################
# class SendChangeUserEmailCodeView(LoginStatusCheck, View):
#     def post(self, request):
#         email = request.POST.get('email')
#         if UserProfile.objects.filter(email=email):
#             return HttpResponse('{"status":"falied", "msg":"该邮箱已经被绑定为其它用户！"}', content_type='application/json')
#         else:
#             send_status = send_email_verificode(email, 'change_email')
#             if send_status:
#                 return HttpResponse('{"status":"success", "msg":"邮件已发送，请注意查收！"}', content_type='application/json')
#             else:
#                 return HttpResponse('{"status":"failed", "msg":"邮件发送失败，请检查！"}', content_type='application/json')
#
# ######################################
# # 修改用户邮箱
# ######################################
# class ChangeUserEmailView(LoginStatusCheck, View):
#     def post(self, request):
#         email = request.POST.get('email')
#         code = request.POST.get('code')
#
#         if (email is not None) and (email != ''):
#             if (code is not None) and (code != ''):
#                 if (len(code) == 4):
#                     code_record = UserEmailVirificationCode.objects.filter(code=code).latest('add_time')
#                     if code_record is not None:
#                         if code_record.email == email:
#                             if (datetime.datetime.now() - code_record.add_time).seconds < 300:
#                                 user = request.user
#                                 user.email = email
#                                 user.save()
#                                 return HttpResponse('{"status":"success", "msg":"邮箱修改成功！"}',
#                                                     content_type='application/json')
#                             else:
#                                 return HttpResponse('{"status":"failed", "msg":"验证码已过期！"}',
#                                                     content_type='application/json')
#                         else:
#                             return HttpResponse('{"status":"failed", "msg":"邮箱错误！"}', content_type='application/json')
#                     else:
#                         return HttpResponse('{"status":"failed", "msg":"验证码错误！"}', content_type='application/json')
#                 else:
#                     return HttpResponse('{"status":"failed", "msg":"验证码错误！"}', content_type='application/json')
#             else:
#                 return HttpResponse('{"status":"failed", "msg":"验证码不能为空！"}', content_type='application/json')
#         else:
#             return HttpResponse('{"status":"failed", "msg":"邮箱不能为空！"}', content_type='application/json')
#

