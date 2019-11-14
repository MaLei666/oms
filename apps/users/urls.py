"""
User app
"""
from django.urls import path,include
from .views import *
from users.apis.user import UserlistApi,UserInfoApi

app_name = 'users'


urlpatterns = [
    # 首页
    path('', IndexView.as_view(), name='index'),

    # 登录
    path('login/', LoginView.as_view(), name='login'),

    # 登出
    path('logout', LogoutView.as_view(), name='logout'),

    # 单位列表
    path('unit/list', UnitListView.as_view(), name='unit_list'),
    # 单位添加
    path('unit/add', AddUnitView.as_view(), name='unit_add'),
    # 单位修改
    path('unit/edit', EditUnitView.as_view(), name='unit_edit'),
    # 单位删除
    path('unit/delete', DeleteUnitView.as_view(), name='unit_delete'),

    # 部门列表
    path('dept/list', DeptListView.as_view(), name='dept_list'),
    # 部门添加
    path('dept/add', AddDeptView.as_view(), name='dept_add'),
    # 部门修改
    path('dept/edit', EditDeptView.as_view(), name='dept_edit'),
    # 部门删除
    path('dept/delete', DeleteDeptView.as_view(), name='dept_delete'),

    # 用户列表
    path('user/list', UserListView.as_view(), name='user_list'),
    # 用户添加
    path('user/add', AddUserView.as_view(), name='user_add'),
    # 用户修改
    path('user/edit', EditUserView.as_view(), name='user_edit'),
    # 用户删除
    path('user/delete', DeleteUserView.as_view(), name='user_delete'),

    # # 用户激活请求
    # path('email/active', SendActiveUserEmailView.as_view(), name='send_active_email'),
    #
    # # 用户激活处理
    # path('active/<str:active_code>', ActiveUserView.as_view(), name='active'),

    # 忘记密码
    path('forget', ForgetPasswordView.as_view(), name='forget'),

    # 重置密码
    path('reset/<str:reset_code>', ResetPasswordView.as_view(), name='reset'),

    # 修改密码
    path('modify', ModifyPasswordView.as_view(), name='modify'),

    # 用户信息
    # path('user/info', UserInfoView.as_view(), name='user_info'),

    # 他人信息
    path('other/user/info/<int:uid>', OtherUserInfoView.as_view(), name='other_user_info'),

    # 修改用户信息
    path('user/info/change', ChangeUserInfoView.as_view(), name='change_user_info'),

    # 用户头像
    path('user/avatar', UserAvatarView.as_view(), name='user_avatar'),

    # 上传修改用户头像
    path('user/avatar/change/upload', ChangeUserAvatarUploadView.as_view(), name='change_user_avatar_upload'),

    # 选择修改用户头像
    path('user/avatar/change/chose', ChangeUserAvatarChoseView.as_view(), name='change_user_avatar_chose'),

    # 用户密码
    path('user/password', UserPasswordView.as_view(), name='user_password'),

    # 修改用户密码
    path('user/password/change', ChangeUserPasswordView.as_view(), name='change_user_password'),

    # 用户邮箱
    path('user/email', UserEmailView.as_view(), name='user_email'),

    # 用户邮箱验证码
    path('user/email/code', SendChangeUserEmailCodeView.as_view(), name='user_email_code'),

    # 修改用户邮箱
    path('user/email/change', ChangeUserEmailView.as_view(), name='change_user_email'),

    # 用户列表
    # path('user/list', UserListView.as_view(), name='user_list'),

    # 添加用户
    path('user/add', AddUserView.as_view(), name='add_user'),

    # 修改用户
    path('user/edit', EditUserView.as_view(), name='edit_user'),

    # 删除用户
    path('user/delete', AddUserView.as_view(), name='delete_user'),

    # 用户登录日志
    path('user/login/record', UserLoginRecordView.as_view(), name='login_record'),

    # 用户操作日志
    path('user/operation/record', UserOperationRecordView.as_view(), name='op_record'),

    # 获取帮助
    # path('help', AskHelpView.as_view(), name='help'),

    #TODO
    path('users/list',UserlistApi.as_view(),name='user_list'),
    path('users/info/<int:user_id>/',UserInfoApi.as_view(),name='user_info')
]


