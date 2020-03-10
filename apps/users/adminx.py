######################################
# Django 模块
######################################
import xadmin
from xadmin.layout import Fieldset
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
    site_footer = u"power by malei"
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
    #                     'url': self.get_model_url(userProfile,'changelist')
    #
    #                 },
    #
    #             )
    #         },
    #
    #     ]

class unitSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('单位信息',
                'name',
                'connect',
                'connect_phone',
                'address',
                'comment',
                'status',
            )
    )
    list_display = ['id','name','connect', 'connect_phone','address','comment','status']
    list_filter = ['name', 'status']
    search_fields = ['name','connect','connect_phone', 'address']
    ordering = ['id']


class deptSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('部门信息',
                 'unit_name',
                 'name',
                 'connect',
                 'connect_phone',
                 'comment',
                 'status',
            )
    )
    list_display = ['id','unit_name','name','connect', 'connect_phone','comment','status']
    list_filter = ['name', 'unit_name','status']
    search_fields = ['name','connect','connect_phone','unit_name']
    ordering = ['id','unit_id']

class loginSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('登录信息',
                 'unit_name',
                 'dept_name',
                 'username',
                 'user_name',
                 'action',
                 'agent',
                 'ip',
                 'address',
                 'add_time',
            )
    )
    list_display = ['id','unit_name','dept_name','username', 'user_name','action','agent','ip','address','add_time']
    list_filter = ['action']
    search_fields = ['unit_name','dept_name','user_name']
    ordering = ['-add_time']


class UserSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('用户信息',
                'role',
                'username',
                'user_name',
                'unit_name',
                'dept_name',
                'mobile',
                'email',
                'gender',
                'position',
                'address',
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
        # Fieldset(None,
        #         #          )
    )
    list_display = ['id','username','user_name', 'role','gender','unit_name','dept_name','position','mobile','email',
                    'status', 'create_time']
    list_filter = ['unit_name','dept_name','gender', 'status']
    search_fields = ['username','user_name','unit_name', 'dept_name', 'mobile','position']
    ordering = ['role','id']



######################################
# 注册
######################################
xadmin.site.unregister(userProfile)
xadmin.site.register(userProfile,UserSetting)
xadmin.site.register(UserLoginInfo,loginSetting)
xadmin.site.register(UserCompany,unitSetting)
xadmin.site.register(UserDepartment,deptSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)
# xadmin.site.register(LogEntry)

