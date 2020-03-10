######################################
# Django 模块
######################################
# from django.contrib import admin
import xadmin
######################################
# 自己写的模块
######################################
from .models import *
from xadmin.layout import Fieldset


class portSetting(object):
    form_layout = (
        Fieldset('端口映射',
                 'unit_name',
                 'dept_name',
                 'ip_out',
                 'port_out',
                 'ip_in',
                 'port_in',
                 'use',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','unit_name','dept_name','ip_out','port_out','ip_in',
                    'port_in','use', 'status','comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','ip_out','port_out','ip_in','port_in']
    ordering = ['-create_time']


class domainNameSetting(object):
    form_layout = (
        Fieldset('域名',
                 'name',
                 'unit_name',
                 'dept_name',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','name','unit_name','dept_name', 'status','comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','name']
    ordering = ['id']



class domainResolveSetting(object):
    form_layout = (
        Fieldset('域名解析',
                 'name',
                 'ip',
                 'domain_name',
                 'unit_name',
                 'dept_name',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','name','ip','domain_name','unit_name','dept_name','status','comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','name','ip']
    ordering = ['id']



class dataDictSetting(object):
    form_layout = (
        Fieldset('数据字典',
                 'name',
                 'value',
                 'type',
                 'description',
                 'sort',
                 'parent_id',
                 'create_time',
                 'create_user',
                 'comment',
            ),
    )
    list_display = ['id','value','type','description','sort','parent_id','create_time','comment']
    search_fields = ['value','type','parent_id']
    ordering = ['id','type','parent_id']
######################################
# 注册
######################################

xadmin.site.register(portToPortInfo,portSetting)
xadmin.site.register(domainNameInfo,domainNameSetting)
xadmin.site.register(domainNameResolveInfo,domainResolveSetting)
xadmin.site.register(dataDictInfo,dataDictSetting)


















