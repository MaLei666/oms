"""
Host management app
"""
from django.urls import path
from system_manage.apis.system_api import *

app_name = 'system_manage'


port_list=portViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
port_detail = portViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

domain_list=domainViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
domain_detail = domainViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

domain_resv_list=domainResvViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
domain_resv_detail = domainResvViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

dict_list=dataDictViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
dict_detail = dataDictViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

urlpatterns = [

    # 端口映射列表
    path('port/list', port_list, name='port_list'),

    # 添加端口映射
    path('port/add', port_list, name='port_add'),

    # 端口映射详情
    path('port/info/<int:pk>', port_detail, name='port_info'),

    # 修改端口映射
    path('port/edit/<int:pk>', port_detail, name='port_edit'),

    # 删除端口映射
    path('port/delete/<int:pk>', port_detail, name='port_del'),

    # 域名列表
    path('domain/list', domain_list, name='domain_list'),

    # 添加域名
    path('domain/add', domain_list, name='domain_add'),

    # 域名详情
    path('domain/info/<int:pk>', domain_detail, name='domain_info'),

    # 编辑域名
    path('domain/edit/<int:pk>', domain_detail, name='domain_edit'),

    # 删除域名
    path('domain/delete/<int:pk>', domain_detail, name='domain_del'),

    # 域名解析列表
    path('domain/resolve/list', domain_resv_list, name='domain_resolve_list'),

    # 添加域名解析
    path('domain/resolve/add', domain_resv_list, name='domain_resolve_add'),

    # 域名解析详情
    path('domain/resolve/info/<int:pk>', domain_resv_detail, name='domain_resolve_info'),

    # 编辑域名解析
    path('domain/resolve/edit/<int:pk>', domain_resv_detail, name='domain_resolve_edit'),

    # 删除域名解析
    path('domain/resolve/delete/<int:pk>', domain_resv_detail, name='domain_resolve_del'),

    #数据字典
    path('dict/list', dict_list, name='dict_list'),

    #添加数据字典
    path('dict/add', dict_list, name='add_dict'),

    # 数据字典详情
    path('dict/info/<int:pk>', dict_detail, name='info_dict'),

    #修改数据字典
    path('dict/edit/<int:pk>', dict_detail, name='edit_dict'),

    #删除数据字典
    path('dict/delete/<int:pk>', dict_detail, name='delete_dict'),

]


