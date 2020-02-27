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
from oms.settings import WEBSSH_IP, WEBSSH_PORT

######################################
# 端口映射列表
######################################
class PortToPortListView(LoginStatusCheck, View):
    def get(self, request):
        if request.user.role <3:
            # 页面选择
            web_chose_left_1 = 'port_domain'
            web_chose_left_2 = 'port_port'
            web_chose_middle = ''

            records = portToPortInfo.objects.filter(status=1).order_by('-update_time')

            # 关键字
            keyword = request.GET.get('keyword', '')
            if keyword != '':
                records = records.filter(
                    Q(ip_in=keyword) | Q(port_in=keyword) | Q(ip_out=keyword) | Q(port_out=keyword) | Q(
                        use__icontains=keyword) | Q(desc__icontains=keyword))

            # 数量
            record_nums = records.count()

            # 判断页码
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            # 对取到的数据进行分页，记得定义每页的数量
            p = Paginator(records, 16, request=request)

            # 分页处理后的 QuerySet
            records = p.page(page)

            context = {
                'web_chose_left_1': web_chose_left_1,
                'web_chose_left_2': web_chose_left_2,
                'web_chose_middle': web_chose_middle,
                'records': records,
                'keyword': keyword,
                'record_nums': record_nums,
            }
            return render(request, 'host_management/port/port_to_port_list.html', context=context)
        else:
            return HttpResponse(status=403)


######################################
# 添加映射
######################################
class AddPortToPortView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            ip_in = request.POST.get('ip_in')
            port_in = request.POST.get('port_in')

            if portToPortInfo.objects.filter(ip_in=ip_in).filter(port_in=port_in).filter(status=1):
                return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            add_port_to_port_form = AddPortToPortForm(request.POST)

            if add_port_to_port_form.is_valid():
                port_info = portToPortInfo()
                port_info.ip_out = request.POST.get('ip_out', '')
                port_info.port_out = request.POST.get('port_out')
                port_info.ip_in = ip_in
                port_info.port_in = port_in
                port_info.use = request.POST.get('use')
                port_info.desc = request.POST.get('desc', '')
                port_info.add_user = request.user
                port_info.update_user = request.user
                port_info.status = 1
                port_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 1
                op_record.status = 1
                op_record.op_num = port_info.id
                op_record.operation = 1
                op_record.action = "添加 [ %s:%s ] 映射：[ %s:%s ]" % (port_info.ip_out, port_info.port_out, port_info.ip_in, port_info.port_in)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"添加映射成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 编辑映射
######################################
class EditPortToPortView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            port_info = portToPortInfo.objects.get(id=int(request.POST.get('p_id')))

            ip_in = request.POST.get('ip_in')
            port_in = request.POST.get('port_in')

            if (port_info.ip_in != ip_in) and (port_info.port_in != port_in):
                if portToPortInfo.objects.filter(ip_in=ip_in).filter(port_in=port_in).filter(status=1):
                    return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            edit_port_to_port_form = EditPortToPortForm(request.POST)

            if edit_port_to_port_form.is_valid():
                port_info.ip_out = request.POST.get('ip_out', '')
                port_info.port_out = request.POST.get('port_out')
                port_info.ip_in = ip_in
                port_info.port_in = port_in
                port_info.use = request.POST.get('use')
                port_info.desc = request.POST.get('desc', '')
                port_info.update_user = request.user
                port_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 1
                op_record.status = 1
                op_record.op_num = port_info.id
                op_record.operation = 2
                op_record.action = "编辑 [ %s:%s ] 映射：[ %s:%s ]" % (port_info.ip_out, port_info.port_out, port_info.ip_in, port_info.port_in)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"编辑映射成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除映射
######################################
class DeletePortToPortView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            port_info = portToPortInfo.objects.get(id=int(request.POST.get('p_id')))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 1
            op_record.status = 1
            op_record.op_num = port_info.id
            op_record.operation = 4
            op_record.action = "停用 [ %s:%s ] 映射：[ %s:%s ]" % (port_info.ip_out, port_info.port_out, port_info.ip_in, port_info.port_in)
            op_record.save()
            port_info.delete()

            return HttpResponse('{"status":"success", "msg":"停用映射成功！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 域名列表
######################################
class DomainNameListView(LoginStatusCheck, View):
    def get(self, request):
        if request.user.role <3:
            # 页面选择
            web_chose_left_1 = 'port_domain'
            web_chose_left_2 = 'domain_name'
            web_chose_middle = ''

            records = domainNameInfo.objects.filter(status=1).order_by('-update_time')

            # 关键字
            keyword = request.GET.get('keyword', '')
            if keyword != '':
                records = records.filter(
                    Q(name__icontains=keyword) | Q(desc__icontains=keyword))

            # 数量
            record_nums = records.count()

            # 判断页码
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            # 对取到的数据进行分页，记得定义每页的数量
            p = Paginator(records, 16, request=request)

            # 分页处理后的 QuerySet
            records = p.page(page)

            context = {
                'web_chose_left_1': web_chose_left_1,
                'web_chose_left_2': web_chose_left_2,
                'web_chose_middle': web_chose_middle,
                'records': records,
                'keyword': keyword,
                'record_nums': record_nums,
            }
            return render(request, 'host_management/port/domain_name_list.html', context=context)
        else:
            return HttpResponse(status=403)


######################################
# 添加域名
######################################
class AddDomainNameView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            name = request.POST.get('name')

            if domainNameInfo.objects.filter(name=name).filter(status=1):
                return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            add_domain_name_form = AddDomainNameForm(request.POST)

            if add_domain_name_form.is_valid():
                domain_info = domainNameInfo()
                domain_info.name = request.POST.get('name')
                domain_info.desc = request.POST.get('desc', '')
                domain_info.add_user = request.user
                domain_info.update_user = request.user
                domain_info.status = 1
                domain_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 1
                op_record.status = 1
                op_record.op_num = domain_info.id
                op_record.operation = 1
                op_record.action = "添加域名：%s" % domain_info.name
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"添加域名成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 修改域名
######################################
class EditDomainNameView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            domain_info = domainNameInfo.objects.get(id=int(request.POST.get('do_id')))

            name = request.POST.get('name')

            if domain_info.name != name:
                if domainNameInfo.objects.filter(name=name).filter(status=1):
                    return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            edit_domain_name_form = EditDomainNameForm(request.POST)

            if edit_domain_name_form.is_valid():
                domain_info.name = request.POST.get('name')
                domain_info.desc = request.POST.get('desc', '')
                domain_info.update_user = request.user
                domain_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 1
                op_record.status = 1
                op_record.op_num = domain_info.id
                op_record.operation = 2
                op_record.action = "修改域名：%s" % domain_info.name
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"修改域名成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除域名
######################################
class DeleteDomainNameView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            domain_info = domainNameInfo.objects.get(id=int(request.POST.get('do_id')))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 1
            op_record.status = 1
            op_record.op_num = domain_info.id
            op_record.operation = 4
            op_record.action = "停用域名：%s" % domain_info.name
            op_record.save()
            domain_info.delete()

            return HttpResponse('{"status":"success", "msg":"停用域名成功！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 域名解析列表
######################################
class DomainNameResolveListView(LoginStatusCheck, View):
    def get(self, request):
        if request.user.role <3:
            # 页面选择
            web_chose_left_1 = 'port_domain'
            web_chose_left_2 = 'domain_resolve'
            web_chose_middle = ''

            records = domainNameResolveInfo.objects.filter(status=1).order_by('-update_time')

            # 关键字
            keyword = request.GET.get('keyword', '')
            if keyword != '':
                records = records.filter(Q(ip=keyword) | Q(domain_name__name__icontains=keyword) | Q(desc__icontains=keyword))

            # 数量
            record_nums = records.count()

            # 判断页码
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            # 对取到的数据进行分页，记得定义每页的数量
            p = Paginator(records, 16, request=request)

            # 分页处理后的 QuerySet
            records = p.page(page)

            domains = domainNameInfo.objects.filter(status=1)

            context = {
                'web_chose_left_1': web_chose_left_1,
                'web_chose_left_2': web_chose_left_2,
                'web_chose_middle': web_chose_middle,
                'records': records,
                'keyword': keyword,
                'record_nums': record_nums,
                'domains': domains,
            }
            return render(request, 'host_management/port/domain_name_resolve_list.html', context=context)
        else:
            return HttpResponse(status=403)


######################################
# 添加域名解析
######################################
class AddDomainNameResolveView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            name = request.POST.get('name')
            domain_name_id = int(request.POST.get('domain_name'))

            if domainNameResolveInfo.objects.filter(name=name).filter(domain_name_id=domain_name_id).filter(status=1):
                return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            add_domain_resolve_form = AddDomainNameResolveForm(request.POST)

            if add_domain_resolve_form.is_valid():
                domain_info = domainNameResolveInfo()
                domain_info.name = name
                domain_info.domain_name_id = domain_name_id
                domain_info.desc = request.POST.get('desc', '')
                domain_info.ip = request.POST.get('ip')
                domain_info.add_user = request.user
                domain_info.update_user = request.user
                domain_info.status = 1
                domain_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 1
                op_record.status = 1
                op_record.op_num = domain_info.id
                op_record.operation = 1
                op_record.action = "添加域名解析：%s" % (domain_info.name)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"添加域名解析成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 修改域名解析
######################################
class EditDomainNameResolveView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            domain_info = domainNameResolveInfo.objects.get(id=int(request.POST.get('do_id')))

            name = request.POST.get('name')
            domain_name_id = int(request.POST.get('domain_name'))

            if (domain_info.name != name) and (domain_info.domain_name_id != domain_name_id):
                if domainNameResolveInfo.objects.filter(name=name).filter(domain_name_id=domain_name_id).filter(status=1):
                    return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            edit_domain_reslove_form = EditDomainNameResolveForm(request.POST)

            if edit_domain_reslove_form.is_valid():
                domain_info.name = name
                domain_info.domain_name_id = domain_name_id
                domain_info.ip = request.POST.get('ip')
                domain_info.desc = request.POST.get('desc', '')
                domain_info.update_user = request.user
                domain_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 1
                op_record.status = 1
                op_record.op_num = domain_info.id
                op_record.operation = 2
                op_record.action = "修改域名解析：%s.%s" % (domain_info.name, domain_info.domain_name.name)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"修改域名解析成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除域名解析
######################################
class DeleteDomainNameResolveView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            domain_info = domainNameResolveInfo.objects.get(id=int(request.POST.get('do_id')))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 1
            op_record.status = 1
            op_record.op_num = domain_info.id
            op_record.operation = 4
            op_record.action = "停用域名解析：%s.%s" % (domain_info.name, domain_info.domain_name.name)
            op_record.save()
            domain_info.delete()

            return HttpResponse('{"status":"success", "msg":"停用域名成功！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)

######################################
# 数据字典列表
######################################
class DictListView(LoginStatusCheck, View):
    def get(self, request):
        if request.user.role <3:
            # 页面选择
            web_chose_left_1 = 'basic_setting'
            web_chose_left_2 = 'dict'
            web_chose_middle = ''

            dicts = dataDictInfo.objects.filter()

            # 数量
            record_nums = dicts.count()

            # 判断页码
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            # 对取到的数据进行分页，记得定义每页的数量
            p = Paginator(dicts, 16, request=request)

            # 分页处理后的 QuerySet
            dicts = p.page(page)


            context = {
                'web_chose_left_1': web_chose_left_1,
                'web_chose_left_2': web_chose_left_2,
                'web_chose_middle': web_chose_middle,
                'dicts': dicts,
                'record_nums': record_nums,
            }
            return render(request, 'host_management/other/data_dict_list.html', context=context)
        else:
            return HttpResponse(status=403)


######################################
# 添加数据字典
######################################
class AddDictView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            name = request.POST.get('name')
            value = request.POST.get('value')

            if dataDictInfo.objects.filter(name=name).filter(value=value):
                return HttpResponse('{"status":"failed", "msg":"该记录已存在，请检查！"}', content_type='application/json')

            add_dict_form = AddDictForm(request.POST)

            if add_dict_form.is_valid():
                dict_info = dataDictInfo()
                dict_info.name = name
                dict_info.value = value
                dict_info.remarks = request.POST.get('remarks', '')
                dict_info.create_by=request.user.id
                dict_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 6
                op_record.status = 1
                op_record.op_num = dict_info.id
                op_record.operation = 1
                op_record.action = "添加数据字典：%s" % (dict_info.name)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"添加域名解析成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 修改数据字典
######################################
class EditDictView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            dict_info = dataDictInfo.objects.get(name=request.POST.get('name'))
            name = request.POST.get('name')
            value = request.POST.get('value')

            if (dict_info.name != name) and (dict_info.value != value):
                if dataDictInfo.objects.filter(name=name).filter(value=value):
                    return HttpResponse('{"status":"failed", "msg":"该数据已存在，请检查！"}', content_type='application/json')

            edit_dict_form = EditDictForm(request.POST)

            if edit_dict_form.is_valid():
                dict_info.name = name
                dict_info.value = value
                dict_info.remarks = request.POST.get('remarks')
                dict_info.save()

                # 添加操作记录
                op_record = UserOperationRecord()
                op_record.op_user = request.user
                op_record.belong = 6
                op_record.status = 1
                op_record.op_num = dict_info.id
                op_record.operation = 2
                op_record.action = "修改数据字典：%s.%s" % (dict_info.name, dict_info.value)
                op_record.save()

                return HttpResponse('{"status":"success", "msg":"修改数据字典成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写不合法，请检查！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)


######################################
# 删除数据字典
######################################
class DeleteDictView(LoginStatusCheck, View):
    def post(self, request):
        if request.user.role <3:
            dict_info = dataDictInfo.objects.get(id=int(request.POST.get('id')))

            # 添加操作记录
            op_record = UserOperationRecord()
            op_record.op_user = request.user
            op_record.belong = 6
            op_record.status = 1
            op_record.op_num = dict_info.id
            op_record.operation = 4
            op_record.action = "删除数据字典：%s.%s" % (dict_info.name, dict_info.value)
            op_record.save()
            dict_info.delete()

            return HttpResponse('{"status":"success", "msg":"删除数据字典成功！"}', content_type='application/json')
        else:
            return HttpResponse(status=403)






