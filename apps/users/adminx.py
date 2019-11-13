######################################
# Django 模块
######################################
# from django.contrib import admin
import xadmin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from xadmin.layout import Row,Fieldset
from xadmin import views
######################################
# 自己写的模块
######################################
from .models import *


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = u"运维管理平台"
    site_footer = u"power by bc"
    menu_style = "accordion"

    # def get_site_menu(self):
    #     return [
    #         {
    #             'title': '自定义菜单',
    #             'icon': 'fa fa-bars',       # Font Awesome图标
    #             'menus':(
    #                 {
    #                     'title': '平台用户',
    #                     'icon': 'fa fa-bug',
    #                     'url': self.get_model_url(UserProfile,'changelist')
    #
    #                 },
    #
    #             )
    #         },
            # {
            #     'title': 'Bug统计',
            #     'icon': 'fa fa-bug',
            #     'menus':(
            #         {
            #             'title': 'Bug表',
            #             'icon': 'fa fa-bug',
            #             'url': "https://www.cnblogs.com/yoyoketang/"  # 自定义跳转列表
            #
            #         },)
            # }

        # ]


class UserSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('用户信息',
                'avatar',
                'role',
                'username',
                'user_name',
                'mobile',
                'email',
                'gender',
                'comment',
            ),
        Fieldset('用户状态',
                'status',
                'is_staff',
                'is_active',
            ),
        Fieldset('用户权限',
                'groups',
                'user_permissions'
            ),
        Fieldset('用户密码',
                'password',
        ),
        Fieldset(None,
                 )
    )
    # fieldsets = (
    #     ('用户信息', {
    #         'fields': (
    #             'avatar',
    #             'role',
    #             'username',
    #             'user_name',
    #             'mobile',
    #             'email',
    #             'gender',
    #             'comment',
    #         )
    #     }),
    #     ('用户状态', {
    #         'fields': (
    #             'status',
    #             'is_staff',
    #             'is_active',
    #
    #         )
    #     }),
    #     ('用户权限', {
    #         'fields': (
    #             'groups',
    #             'user_permissions'
    #         )
    #     }),
    #     ('用户密码', {
    #         'fields': (
    #             'password',
    #         )
    #     }),
    # )
    list_display = ('id','username','user_name', 'role','gender','unit_name','dept_name','mobile','email', 'status', 'create_time')
    list_filter = ('is_staff', 'gender', 'is_active', 'groups')
    search_fields = ('username','user_name','unit_name', 'dept_name', 'mobile')
    ordering = ('role',)



######################################
# 注册
######################################
xadmin.site.register(UserCompany)
xadmin.site.register(UserDepartment)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserSetting)
xadmin.site.register(UserEmailVirificationCode)
xadmin.site.register(UserLoginInfo)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)
# xadmin.site.register(LogEntry)

