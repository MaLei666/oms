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
xadmin.site.register(operatSystemInfo)
xadmin.site.register(idcInfo)
xadmin.site.register(rackInfo)
xadmin.site.register(useInfo)
xadmin.site.register(projectInfo)
xadmin.site.register(hostInfo)
xadmin.site.register(hostServiceInfo)
xadmin.site.register(databaseInfo)
xadmin.site.register(databaseDBInfo)


















