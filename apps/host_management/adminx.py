######################################
# Django 模块
######################################
import xadmin
from xadmin.layout import Fieldset

######################################
# 自己写的模块
######################################
from .models import *


class osSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('操作系统',
                'name',
                'version',
                'bit',
                'create_time',
                'create_user',
                'comment',
                'status',
            ),
    )
    list_display = ['id','name','version','bit','create_time','create_user','status', 'comment']
    list_filter = ['bit', 'status']
    search_fields = ['name','version']
    ordering = ['id']


class projectSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('项目',
                 'unit_name',
                 'name',
                 'op_user',
                 'run_env',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','unit_name','name','op_user','run_env','create_time','create_user','status', 'comment']
    list_filter = ['status']
    search_fields = ['unit_name','name','op_user']
    ordering = ['id']


class useSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('用途',
                 'name',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','name','create_time','create_user','status', 'comment']
    list_filter = ['status']
    search_fields = ['name']
    ordering = ['id']


class idcSetting(object):
    form_layout = (
        Fieldset('机房',
                 'unit_name',
                 'name',
                 'isp',
                 'line',
                 'bandwidth',
                 'racks',
                 'address',
                 'connect',
                 'connect_phone',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','unit_name','name','isp','line','bandwidth','racks','address','connect',
                    'connect_phone','status', 'comment']
    list_filter = ['status']
    search_fields = ['unit_name','name','isp','line','bandwidth','racks']
    ordering = ['id']


class rackSetting(object):
    form_layout = (
        Fieldset('机柜',
                 'unit_name',
                 'dept_name',
                 'idc_name',
                 'name',
                 'number',
                 'height',
                 'power',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','unit_name','dept_name','idc_name','name','number','height','power','status', 'comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','name','idc_name','number','height','power']
    ordering = ['id']


class hostSetting(object):
    form_layout = (
        Fieldset('主机',
                 'in_ip',
                 'out_ip',
                 'system',
                 'unit_name',
                 'dept_name',
                 'idc_name',
                 'rack_name',
                 'address',
                 'disk',
                 'memory',
                 'network',
                 'ssh_port',
                 'root_ssh',
                 'disk',
                 'use',
                 'project',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','in_ip','out_ip','system','unit_name','dept_name','idc_name','rack_name','address',
                    'use','project', 'status','comment']
    list_filter = ['status','system','use','project']
    search_fields = ['unit_name','dept_name','rack_name','idc_name','in_ip','out_ip']
    ordering = ['id']


class hostServiceSetting(object):
    form_layout = (
        Fieldset('主机',
                 'hostname'
                 'in_ip',
                 'out_ip',
                 'unit_name',
                 'dept_name',
                 'name',
                 'version',
                 'listen_user',
                 'listen_port',
                 'ins_path',
                 'log_path',
                 'backup_path',
                 'start_cmd',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','in_ip','out_ip','unit_name','dept_name','name','version','listen_user',
                    'listen_port', 'status','comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','name','in_ip','out_ip','listen_port']
    ordering = ['id']



class dbSetting(object):
    form_layout = (
        Fieldset('主机',
                 'in_ip',
                 'out_ip',
                 'hostname',
                 'unit_name',
                 'dept_name',
                 'db_name',
                 'db_version',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','in_ip','out_ip','hostname','unit_name','dept_name','db_name','db_version','status','comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','db_name','db_version','in_ip','out_ip']
    ordering = ['id']


class dbDBSetting(object):
    form_layout = (
        Fieldset('主机',
                 'hostname',
                 'unit_name',
                 'dept_name',
                 'db_name',
                 'name',
                 'use',
                 'create_time',
                 'create_user',
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','hostname','unit_name','dept_name','db_name','name','use','status','comment']
    list_filter = ['status']
    search_fields = ['unit_name','dept_name','db_name','name']
    ordering = ['id']
######################################
# 注册
######################################
xadmin.site.register(operatSystemInfo,osSetting)
xadmin.site.register(idcInfo,idcSetting)
xadmin.site.register(rackInfo,rackSetting)
xadmin.site.register(useInfo,useSetting)
xadmin.site.register(projectInfo,projectSetting)
xadmin.site.register(hostInfo,hostSetting)
xadmin.site.register(hostServiceInfo,hostServiceSetting)
xadmin.site.register(databaseInfo,dbSetting)
xadmin.site.register(databaseDBInfo,dbDBSetting)


















