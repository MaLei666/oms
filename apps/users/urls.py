"""
User app
"""
from django.urls import path,include
from users.apis.user_api import *
from rest_framework_jwt.views import obtain_jwt_token

__all__=['urlpatterns','app_name']

app_name = 'users'

user_list=UserViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
users_detail = UserViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

unit_list=unitViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
unit_detail = unitViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

dept_list=deptViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
dept_detail = deptViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

login_list=logininfoView.as_view({
    'get': 'list',

})

oprea_list=operationView.as_view({
    'get': 'list',

})

urlpatterns = [

    # 登录
    path('login/', obtain_jwt_token, name='login'),

    # 登出
    path('logout/', logout_view.as_view(), name='logout'),

    # 单位列表
    path('unit/list', unit_list, name='unit_list'),
    # 单位添加
    path('unit/add', unit_list, name='unit_add'),
    # 单位详情
    path('unit/info/<int:pk>', unit_detail, name='unit_info'),
    # 单位修改
    path('unit/edit/<int:pk>',unit_detail, name='unit_edit'),
    # 单位删除
    path('unit/delete/<int:pk>', unit_detail, name='unit_delete'),

    # 部门列表
    path('dept/list', dept_list, name='dept_list'),
    # 部门添加
    path('dept/add', dept_list, name='dept_add'),
    # 部门详情
    path('dept/info/<int:pk>', dept_detail, name='dept_info'),
    # 部门修改
    path('dept/edit/<int:pk>', dept_detail, name='dept_edit'),
    # 部门删除
    path('dept/delete/<int:pk>', dept_detail, name='dept_delete'),

    # 用户列表
    path('user/list', user_list, name='user_list'),
    # 用户详情
    path('user/info/<int:pk>', users_detail, name='user_info'),
    # 用户添加
    path('user/add', user_list, name='user_add'),
    # 用户修改
    path('user/edit/<int:pk>', users_detail, name='user_edit'),
    # 用户删除
    path('user/delete/<int:pk>', users_detail, name='user_delete'),
    # 修改密码
    # path('modify', ModifyPasswordView.as_view(), name='modify'),
    # 用户密码
    # path('user/password', UserPasswordView.as_view(), name='user_password'),

    # 修改用户密码
    path('user/password/change', change_pw_view.as_view(), name='change_user_password'),

    # # 用户邮箱
    # path('user/email', UserEmailView.as_view(), name='user_email'),
    #
    # # 用户邮箱验证码
    # path('user/email/code', SendChangeUserEmailCodeView.as_view(), name='user_email_code'),
    #
    # # 修改用户邮箱
    # path('user/email/change', ChangeUserEmailView.as_view(), name='change_user_email'),

    # 用户登录日志
    path('user/login/record', login_list, name='login_record'),

    # 用户操作日志
    path('user/operation/record', oprea_list, name='op_record'),

    # 获取帮助
    # path('help', AskHelpView.as_view(), name='help'),

]


