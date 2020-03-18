"""
Host management app
"""
from django.urls import path
from platform_management.apis.plat_api import *

plat_list=platViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
plat_detail = platViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

platuser_list=platUserViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
platuser_detail = platUserViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

app_name = 'platform_management'

urlpatterns = [
    # 平台列表
    path('list', plat_list, name='platform_list'),

    # 添加平台
    path('add', plat_list, name='platform_add'),

    # 平台详情
    path('info/<int:plat_id>', plat_detail, name='platform_info'),

    # 编辑平台
    path('edit/<int:plat_id>', plat_detail, name='platform_edit'),

    # 删除平台
    path('delete/<int:plat_id>', plat_detail, name='platform_delete'),

    # 平台用户列表
    path('user/list', platuser_list, name='platuser_list'),

    # 添加平台用户
    path('user/add', platuser_list, name='platuser_add'),

    # 平台用户详情
    path('user/info/<int:platuser_id>', platuser_detail, name='platuser_info'),

    # 编辑用户平台
    path('user/edit/<int:platuser_id>', platuser_detail, name='platuser_edit'),

    # 删除平台用户
    path('user/delete/<int:platuser_id>', platuser_detail, name='platuser_delete'),


]


