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

xadmin.site.register(portToPortInfo)
xadmin.site.register(domainNameInfo)
xadmin.site.register(domainNameResolveInfo)
xadmin.site.register(dataDictInfo)


















