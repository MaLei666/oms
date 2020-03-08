"""
Document management app
"""
from django.urls import path
from document_management.apis.document_api import *

app_name = 'document_management'


doc_list=docViewSet.as_view({
            'get': 'list',
            'post': 'create'
            }
        )
doc_detail = docViewSet.as_view({
            'get':'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        })

urlpatterns = [
    # 文档列表
    path('list', doc_list, name='doc_list'),

    # 添加文档
    path('add', doc_list, name='doc_add'),

    # 文档详情
    path('info/<int:doc_id>', doc_detail, name='doc_detail'),

    # 修改文档
    path('edit/<int:doc_id>', doc_detail, name='doc_edit'),

    # 删除文档
    path('delete/<int:doc_id>', doc_detail, name='doc_del'),

    # 脚本下载
    # path('script/download/<int:doc_id>', DocumentDownloadView, name='doc_script_download'),
]
