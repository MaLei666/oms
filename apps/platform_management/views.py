######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage

######################################
# 系统模块
######################################
import json
import datetime

######################################
# 自建模块
######################################
from utils.login_check import LoginStatusCheck
from .forms import *
from .models import *
from operation_record.models import UserOperationRecord


######################################
# 内部平台列表
######################################
class CompanyPlatformListView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'platform'
        web_chose_left_2 = 'unit'
        web_chose_middle = ''

        title = '内部平台'

        platforms = PlatformInfo.objects.filter(belong=1)

        platform_nums = platforms.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(platforms, 17, request=request)

        # 分页处理后的 QuerySet
        platforms = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'title': title,
            'platforms': platforms,
            'platform_nums': platform_nums,
        }
        return render(request, 'platform-management/platform_list.html', context=context)

######################################
# 添加内部平台
######################################
class AddCompanyPlatformView(LoginStatusCheck, View):
    def post(self, request):
        try:
            name = request.POST.get("name", "")
            url = request.POST.get("url", "")
            if (name != "") and (url != ""):
                plat_obj = PlatformInfo()
                plat_obj.name = name
                plat_obj.url = url
                plat_obj.belong = 1
                plat_obj.add_user = request.user
                plat_obj.save()
                return HttpResponse('{"status":"success", "msg":"添加内部平台成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写错误！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"未知错误！"}', content_type='application/json')

######################################
# 修改平台
######################################
class EditPlatInfoView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role > 1:
            edit_host_info_form = EditPlatformForm(request.POST)
            if edit_host_info_form.is_valid():

                # 获取主机
                plat = PlatformInfo.objects.get(id=int(request.POST.get('plat_id')))
                plat.name = request.POST.get('name')
                plat.url = request.POST.get('url')
                plat.save()

                # # 添加操作记录
                # op_record = UserOperationRecord()
                # op_record.op_user = request.user
                # op_record.belong = 1
                # op_record.status = 1
                # op_record.op_num = plat.id
                # op_record.operation = 2
                # op_record.action = "修改平台：%s" % plat.name
                # op_record.save()

                return HttpResponse('{"status":"success", "msg":"平台信息修改成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"平台信息填写错误，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除平台
######################################
class DeletePlatformView(LoginStatusCheck, View):
    def post(self, request):
        try:
            plat_id = request.POST.get('plat_id')
            plat = PlatformInfo.objects.get(id=int(plat_id))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 1
            op_record.status = 1
            op_record.op_num = plat.id
            op_record.operation = 4
            op_record.action = "删除平台：%s" % (plat.name)
            op_record.save()
            plat.delete()
            return HttpResponse('{"status":"success", "msg":"平台删除成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"falied", "msg":"平台删除失败！"}', content_type='application/json')

######################################
# 添加平台用户列表
######################################
class EditPlatformUserView(LoginStatusCheck, View):
    def post(self, request):
        try:
            pu_id = request.POST.get('pu_id', '')
            if pu_id != '':
                pu = PlatformUserInfo.objects.get(id=int(pu_id))
                pu.username = request.POST.get('username', '')
                pu.password = request.POST.get('password', '')
                pu.update_user = request.user
                pu.save()
            else:
                platform_id = int(request.POST.get('platform_id'))
                pu = PlatformUserInfo()
                pu.platform_id = platform_id
                pu.username = request.POST.get('username', '')
                pu.password = request.POST.get('password', '')
                pu.user = request.user
                pu.update_user = request.user
                pu.save()

            return HttpResponse('{"status":"success", "msg":"修改用户成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"修改用户失败！"}', content_type='application/json')


######################################
# 其它平台列表
######################################
class OtherPlatformListView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'platform'
        web_chose_left_2 = 'other'
        web_chose_middle = ''

        title = '其它平台'

        platforms = PlatformInfo.objects.filter(belong=2)

        platform_nums = platforms.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(platforms, 17, request=request)

        # 分页处理后的 QuerySet
        platforms = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'title': title,
            'platforms': platforms,
            'platform_nums': platform_nums,
        }
        return render(request, 'platform-management/user_platform_list.html', context=context)


######################################
# 添加其它平台
######################################
class AddOtherPlatformView(LoginStatusCheck, View):
    def post(self, request):
        try:
            name = request.POST.get("name", "")
            url = request.POST.get("url", "")


            if (name != "") and (url != ""):
                plat_obj = PlatformInfo()
                plat_obj.name = name
                plat_obj.url = url
                plat_obj.belong = 2
                plat_obj.add_user = request.user
                plat_obj.save()
                return HttpResponse('{"status":"success", "msg":"添加个人平台成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写错误！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"未知错误！"}', content_type='application/json')

