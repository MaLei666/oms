from ..models import *
from django import template

register = template.Library()

# 获取主机数量
@register.simple_tag
def Get_Host_Nums():
    return hostInfo.objects.filter(status=1).count()

@register.simple_tag
def Get_Db_Nums():
    return databaseInfo.objects.filter(status=1).count()

@register.simple_tag
def Get_Port_Nums():
    return portToPortInfo.objects.filter(status=1).count()

@register.simple_tag
def Get_Domin_Nums():
    return domainNameResolveInfo.objects.filter(status=1).count()