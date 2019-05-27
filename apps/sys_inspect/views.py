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
from host_management.models import DataDictInfo

######################################
# 巡检设备列表
######################################
class InspectDevInfoViews(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'inspect'
        web_chose_left_2 = 'devices'
        web_chose_middle = ''

        title = '设备列表'

        devices = InspectDevInfo.objects.filter()
        # 用户
        users = UserProfile.objects.filter()

        # 部门
        depts=UserDepartment.objects.filter()

        # 公司
        units = UserCompany.objects.filter()

        # 数据字典
        dicts=DataDictInfo.objects.filter()

        devices_nums = devices.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(devices, 17, request=request)

        # 分页处理后的 QuerySet
        devices = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'title': title,
            'devices': devices,
            'depts':depts,
            'devices_nums': devices_nums,
            'users':users,
            'units': units,
            'dicts':dicts
        }
        return render(request, 'sys_inspect/inspect_dev_list.html', context=context)

######################################
# 添加设备
######################################
class AddDevView(LoginStatusCheck, View):
    def post(self, request):

        if request.user.role < 3:
            add_dev_form = AddDevForm(request.POST)
            if add_dev_form.is_valid():
                dev_id = request.POST.get('dev_id')

                if InspectDevInfo.objects.filter(dev_id=dev_id).filter():
                    return HttpResponse('{"status":"failed", "msg":"该设备id已经存在，请检查！"}',
                                        content_type='application/json')

                device = InspectDevInfo()
                device.unit_id = request.POST.get('unit_id')
                device.unit_name=UserCompany.objects.get(id=request.POST.get('unit_id'))
                device.dev_id = dev_id
                device.dev_name = request.POST.get('dev_name')
                device.dev_type=request.POST.get('dev_type')
                device.install_position = request.POST.get('install_position')
                device.comment = request.POST.get('comment')
                device.create_mobile=request.user.mobile
                device.create_user=request.user.id
                device.create_time=datetime.datetime.now()
                device.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 5
                op_record.status = 1
                op_record.op_num = device.id
                op_record.operation = 1
                op_record.action = "添加巡检设备：%s：%s" % (device.dev_id,device.dev_name)
                op_record.save()
                return HttpResponse('{"status":"success", "msg":"巡检设备添加成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"巡检设备填写错误，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)
#
######################################
# 修改设备
######################################
class EditDevInfoView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role < 3:
            edit_dev_info_form = EditDevForm(request.POST)
            if edit_dev_info_form.is_valid():

                # 获取设备
                device = InspectDevInfo.objects.get(id=request.POST.get('id'))
                device.dev_name = request.POST.get('dev_name')
                device.install_position = request.POST.get('install_position')
                device.comment = request.POST.get('comment')
                device.status= request.POST.get('status')
                device.update_user=request.user.id
                device.update_time=datetime.datetime.now()

                device.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 5
                op_record.status = 1
                op_record.op_num = device.id
                op_record.operation = 2
                op_record.action = "修改巡检设备：%s:%s" % (device.dev_id,device.dev_name)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"巡检设备信息修改成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"巡检设备信息填写错误，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除设备
######################################
class DeleteDevView(LoginStatusCheck, View):
    def post(self, request):
        try:
            device = InspectDevInfo.objects.get(id=request.POST.get('id'))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 5
            op_record.status = 1
            op_record.op_num = device.id
            op_record.operation = 4
            op_record.action = "删除巡检设备设备：%s：%s" % (device.dev_id,device.dev_name)
            op_record.save()
            device.delete()
            return HttpResponse('{"status":"success", "msg":"巡检设备删除成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"falied", "msg":"巡检设备删除失败！"}', content_type='application/json')


######################################
# 巡检内容列表
######################################
class ContentViews(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'inspect'
        web_chose_left_2 = 'contents'
        web_chose_middle = ''

        title = '任务列表'
        # 用户
        users = UserProfile.objects.filter()

        # 部门
        depts = UserDepartment.objects.filter()

        #公司
        units=UserCompany.objects.filter()

        #设备
        devices=InspectDevInfo.objects.filter()

        contents = InspectContentInfo.objects.filter()

        contents_nums = contents.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(contents, 20, request=request)

        # 分页处理后的 QuerySet
        contents = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'title': title,
            'contents': contents,
            'contents_nums': contents_nums,
            'depts': depts,
            'users': users,
            'units':units,
            'devices':devices
        }
        return render(request, 'sys_inspect/inspect_content_list.html', context=context)

######################################
# 添加任务
######################################
class AddContView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role < 3:
            add_cont_form = AddContForm(request.POST)
            if add_cont_form.is_valid():
                content = InspectContentInfo()
                content.task_name = request.POST.get('taskName')
                content.task_type = request.POST.get('taskType')
                content.dept_id= request.POST.get('deptId')
                content.unit_id=request.POST.get('unitId')
                content.user_id=request.POST.get('userId')


                content.start_time = request.POST.get('startTime')
                content.end_time = request.POST.get('endTime')
                content.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 5
                op_record.status = 1
                op_record.op_num = content.id
                op_record.operation = 1
                op_record.action = "添加巡检任务：%s" % (content.task_name)
                op_record.save()
                return HttpResponse('{"status":"success", "msg":"巡检任务添加成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"巡检任务填写错误，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除任务
######################################
class DeleteContView(LoginStatusCheck, View):
    def post(self, request):
        try:
            dev_id = request.POST.get('dev_id')
            device = InspectDevInfo.objects.get(id=int(dev_id))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 5
            op_record.status = 1
            op_record.op_num = device.id
            op_record.operation = 4
            op_record.action = "删除巡检设备设备：%s：%s" % (device.dev_id,device.dev_name)
            op_record.save()
            device.delete()
            return HttpResponse('{"status":"success", "msg":"巡检设备删除成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"falied", "msg":"巡检设备删除失败！"}', content_type='application/json')

