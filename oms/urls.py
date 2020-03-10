from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls import url
from oms.settings import MEDIA_ROOT
from django.views.static import serve
from document_management.views import upload_image
from django.conf import settings
import xadmin
import rest_framework


# 错误页面
handler403 = 'users.views.permission_denied'
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),

    # 静态文件
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    # media 配置
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # users
    path('', include('users.urls',namespace='users')),

    # host management
    path('host/', include('host_management.urls')),

    # system_manage
    path('system/',include('system_manage.urls')),

    # platform management
    path('platform/', include('platform_management.urls')),

    # message
    # path('message/', include('message.urls')),

    # document management
    path('document/', include('document_management.urls')),

    # CKeditor上传图片
    path('uploadimg/', upload_image),

    # online
    # path('online/', include('online_management.urls')),


]


