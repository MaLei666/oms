######################################
# Django 模块
######################################
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
        ('用户密码', {
            'fields': (
                'password',
            )
        }),
    )


######################################
# 注册
######################################
admin.site.register(UserCompany)
admin.site.register(UserDepartment)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(UserEmailVirificationCode)
admin.site.register(UserLoginInfo)