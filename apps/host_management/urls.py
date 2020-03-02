"""
Host management app
"""
from django.urls import path
from host_management.apis.host_api import *


app_name = 'host_management'


os_list=osViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
os_detail = osViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

project_list=projectViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
project_detail = projectViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

use_list=useViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
use_detail = useViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

idc_list=idcViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
idc_detail = idcViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

rack_list=rackViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
rack_detail = rackViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

host_list=hostViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
host_detail = hostViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

host_service_list=hostserviceViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
host_service_detail = hostserviceViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

database_list=databaseViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
database_detail = databaseViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })


databaseDB_list=databaseDBViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
databaseDB_detail = databaseDBViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

urlpatterns = [
    # 操作系统列表
    path('os/list', os_list, name='os_list'),

    # 添加系统
    path('os/add', os_list, name='add_os'),

    # 系统详情
    path('os/info/<int:system_id>', os_detail, name='os_info'),

    # 修改系统
    path('os/edit/<int:system_id>', os_detail, name='edit_os'),

    # 删除系统
    path('os/delete/<int:system_id>', os_detail, name='del_os'),

    # 项目列表
    path('project/list', project_list, name='project_List'),

    # 添加项目
    path('project/add', project_list, name='add_project'),

    # 项目详情
    path('project/info/<int:project_id>', project_detail, name='info_project'),

    # 编辑项目
    path('project/edit/<int:project_id>', project_detail, name='edit_project'),

    # 删除项目
    path('project/delete/<int:project_id>', project_detail, name='del_project'),

    # 用途列表
    path('use/list', use_list, name='use_List'),

    # 添加用途
    path('use/add', use_list, name='add_use'),

    # 修改用途
    path('use/edit/<int:use_id>', use_detail, name='edit_use'),

    # 删除用途
    path('use/delete/<int:use_id>', use_detail, name='del_use'),

    # 机房列表
    path('idc/list', idc_list, name='idc_list'),

    # 添加机房
    path('idc/add', idc_list, name='idc_host'),

    # 机房详情
    path('idc/info/<int:idc_id>', idc_detail, name='idc_info'),

    # 修改机房
    path('idc/edit/<int:idc_id>', idc_detail, name='idc_host'),

    # 删除机房
    path('idc/delete/<int:idc_id>', idc_detail, name='idc_host'),

    # 机柜列表
    path('rack/list', rack_list, name='rack_list'),

    # 添加机柜
    path('rack/add', rack_list, name='add_rack'),

    # 机柜详情
    path('rack/info/<int:rack_id>', rack_detail, name='rack_info'),

    # 修改机柜
    path('rack/edit/<int:rack_id>', rack_detail, name='edit_rack'),

    # 删除机柜
    path('rack/delete/<int:rack_id>', rack_detail, name='del_rack'),

    # # webssh
    # path(r'webssh/<int:host_id>', WebSSHView, name='web_ssh'),

    # 主机列表
    path('host/list', host_list, name='host_list'),

    # 添加主机
    path('host/add', host_list, name='add_host'),

    # 主机详情
    path('host/info/<int:host_id>', host_detail, name='host_info'),

    # 修改主机
    path('host/edit/<int:host_id>', host_detail, name='edit_host'),

    # 删除主机
    path('host/delete/<int:host_id>', host_detail, name='del_host'),

    # 主机服务列表
    path('service/list', host_service_list, name='list_host_service'),

    # 添加主机服务
    path('service/add', host_service_list, name='add_host_service'),

    # 服务详情
    path('service/info/<int:host_service_id>', host_service_detail, name='info_host_service'),

    # 修改主机服务
    path('service/edit/<int:host_service_id>', host_service_detail, name='edit_host_service'),

    # 删除主机服务
    path('service/delete/<int:host_service_id>', host_service_detail, name='del_host_service'),

    # 数据库连接列表
    path('database/list', database_list, name='db_list'),

    # 数据库连接详情
    path('database/info/<int:db_id>', database_detail, name='db_info'),

    # 添加数据库信息
    path('database/add', database_list, name='add_db'),

    # 修改数据库信息
    path('database/edit/<int:db_id>', database_detail, name='edit_db'),

    # 删除数据库信息
    path('database/delete/<int:db_id>', database_detail, name='del_db'),

    # 数据库列表
    path('database/db/list', databaseDB_list, name='db_list'),

    # 数据库详情
    path('database/db/info/<int:db_db_id>', databaseDB_detail, name='db_info'),

    # 添加数据库库表
    path('database/db/add', databaseDB_list, name='add_db_db'),

    # 修改数据库库表
    path('database/db/edit/<int:db_db_id>', databaseDB_detail, name='edit_db_db'),

    # 删除数据库库表
    path('database/db/delete/<int:db_db_id>', databaseDB_detail, name='del_db_db'),

    # # 添加数据库用户
    # path('database/user/add', AddDatabaseUserView, name='add_db_user'),
    #
    # # 修改数据库用户
    # path('database/user/edit', EditDatabaseUserView, name='edit_db_user'),
    #
    # # 删除数据库用户
    # path('database/user/delete', DeleteDatabaseUserView, name='del_db_user'),
    #
    # # 操作记录
    # path('operation/record', HostOperationView, name='host_op_record'),



]


