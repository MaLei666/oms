######################################
# Django 模块
######################################
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry

######################################
# 自己写的模块
######################################
from .models import *


class UserAdmin(UserAdmin):

    # fieldsets=()
    fieldsets = (
        ( '用户信息',{
            'fields':(
                'avatar',
                'role',
                'username',
                'user_name',
                'mobile',
                'email',
                'gender',
                'comment',
            )
        }),
        ( '用户状态',{
            'fields':(
                'status',
                'is_staff',
                'is_active',

            )
        }),
        ('用户权限',{
            'fields':(
                'groups',
                'user_permissions'
            )
        }),
        ('用户密码', {
            'fields': (
                'password',
            )
        }),
    )
    list_display = ('id','username','user_name', 'role','gender','unit_name','dept_name','mobile','email', 'status', 'create_time')
    list_filter = ('is_staff', 'gender', 'is_active', 'groups')
    search_fields = ('username','user_name','unit_name', 'dept_name', 'mobile')
    ordering = ('role',)



######################################
# 注册
######################################
admin.site.register(UserCompany)
admin.site.register(UserDepartment)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(UserEmailVirificationCode)
admin.site.register(UserLoginInfo)

admin.site.register(LogEntry)