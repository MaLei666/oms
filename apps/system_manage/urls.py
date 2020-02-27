"""
Host management app
"""
from django.urls import path
from system_manage.views import *


app_name = 'system_manage'

urlpatterns = [

    # 端口映射列表
    path('port/to/port/list', PortToPortListView.as_view(), name='port_port_list'),

    # 添加端口映射
    path('port/to/port/add', AddPortToPortView.as_view(), name='port_port_add'),

    # 修改端口映射
    path('port/to/port/edit', EditPortToPortView.as_view(), name='port_port_edit'),

    # 删除端口映射
    path('port/to/port/delete', DeletePortToPortView.as_view(), name='port_port_del'),

    # 域名列表
    path('domainname/list', DomainNameListView.as_view(), name='domain_name_list'),

    # 添加域名
    path('domainname/add', AddDomainNameView.as_view(), name='domain_name_add'),

    # 编辑域名
    path('domainname/edit', EditDomainNameView.as_view(), name='domain_name_edit'),

    # 删除域名
    path('domainname/delete', DeleteDomainNameView.as_view(), name='domain_name_del'),

    # 域名解析列表
    path('domainname/resolve/list', DomainNameResolveListView.as_view(), name='domain_resolve_list'),

    # 添加域名解析
    path('domainname/resolve/add', AddDomainNameResolveView.as_view(), name='domain_resolve_add'),

    # 编辑域名解析
    path('domainname/resolve/edit', EditDomainNameResolveView.as_view(), name='domain_resolve_edit'),

    # 删除域名解析
    path('domainname/resolve/delete', DeleteDomainNameResolveView.as_view(), name='domain_resolve_del'),

    #数据字典
    path('dict/list', DictListView.as_view(), name='dict_list'),

    #添加数据字典
    path('dict/add', AddDictView.as_view(), name='add_dict'),

    #修改数据字典
    path('dict/edit', EditDictView.as_view(), name='edit_dict'),

    #删除数据字典
    path('dict/delete', DeleteDictView.as_view(), name='delete_dict'),

]


