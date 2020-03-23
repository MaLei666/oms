# from django.contrib import admin
from .models import *
import xadmin
from xadmin.layout import Fieldset

class platSetting(object):
    form_layout = (
        Fieldset('name',
                 'url',
                 'belong',
                 'unit_name',
                 'dept_name',
                 'create_user',
                 'create_time',
                 'update_user',
                 'update_time'
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','name','url','belong','unit_name','dept_name','create_user','create_time',
                    'comment', 'status']
    list_filter = ['status','belong']
    search_fields = ['name','url','unit_name','dept_name']
    ordering = ['id']

class platUserSetting(object):
    form_layout = (
        Fieldset('platform',
                 'unit_name',
                 'dept_name',
                 'username',
                 'password',
                 'create_user',
                 'create_time',
                 'update_user',
                 'update_time'
                 'comment',
                 'status',
            ),
    )
    list_display = ['id','platform','unit_name','dept_name','create_user','create_time',
                    'comment', 'status']
    list_filter = ['status']
    search_fields = ['platform','unit_name','dept_name']
    ordering = ['id']

# Register your models here.
xadmin.site.register(platformInfo,platSetting)
xadmin.site.register(platformUserInfo,platUserSetting)