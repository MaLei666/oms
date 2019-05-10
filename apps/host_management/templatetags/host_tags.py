from ..models import *
from django import template

register = template.Library()

# 获取主机数量
@register.simple_tag
def Get_Host_Nums():
    return HostInfo.objects.filter(status=1).count()

@register.simple_tag
def Get_Db_Nums():
    return DatabaseInfo.objects.filter(status=1).count()

@register.simple_tag
def Get_Port_Nums():
    return PortToPortInfo.objects.filter(status=1).count()

@register.simple_tag
def Get_Domin_Nums():
    return DomainNameResolveInfo.objects.filter(status=1).count()