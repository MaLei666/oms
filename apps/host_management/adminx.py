######################################
# Django 模块
######################################
# from django.contrib import admin
import xadmin
######################################
# 自己写的模块
######################################
from .models import *

######################################
# 注册
######################################
xadmin.site.register(OperatingSystemInfo)
# xadmin.site.register(OperatingEnvironmentInfo)
# xadmin.site.register(IdcInfo)
xadmin.site.register(UseInfo)
xadmin.site.register(ProjectInfo)
xadmin.site.register(HostInfo)
xadmin.site.register(HostServiceInfo)
xadmin.site.register(DatabaseInfo)
xadmin.site.register(DatabaseDBInfo)
xadmin.site.register(DatabaseUserInfo)
# xadmin.site.register(NetworkDviceInfo)
xadmin.site.register(PortToPortInfo)
xadmin.site.register(DomainNameInfo)
xadmin.site.register(DomainNameResolveInfo)


















