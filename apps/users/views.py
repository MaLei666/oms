######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views import View
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


#
# ######################################
# # 重置修改密码
# ######################################
# class ModifyPasswordView(View):
#     def post(self, request):
#         new_password = request.POST.get('new_password')
#         renew_password = request.POST.get('renew_password')
#         reset_code = request.POST.get('reset_code')
#         if new_password != renew_password:
#             msg = '密码不一致！'
#             context = {
#                 'msg': msg,
#                 'reset_code': reset_code
#             }
#             return render(request, 'users/login/reset_password.html', context=context)
#         elif (len(new_password) < 6) or (len(new_password) > 20):
#             msg = '密码长度不符合要求！'
#             context = {
#                 'msg': msg,
#                 'reset_code': reset_code
#             }
#             return render(request, 'users/login/reset_password.html', context=context)
#         else:
#             # 获取相应的用户
#             code_record = UserEmailVirificationCode.objects.filter(code=reset_code).latest('add_time')
#             email = code_record.email
#             user = userProfile.objects.get(email=email)
#
#             # 修改密码
#             try:
#                 user.password = make_password(new_password)
#                 user.save()
#
#                 # 修改验证码状态
#                 code_record.is_use = True
#                 code_record.save()
#
#                 msg = '密码重置成功！'
#                 context = {
#                     'msg': msg,
#                 }
#                 return render(request, 'users/login/login.html', context=context)
#             except Exception as e:
#                 msg = '密码重置失败，请重试！'
#                 context = {
#                     'msg': msg,
#                     'reset_code': reset_code
#                 }
#                 return render(request, 'users/login/reset_password.html', context=context)


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
#         if userProfile.objects.filter(email=email):
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
