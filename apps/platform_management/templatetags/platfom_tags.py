from ..models import *
from django import template

register = template.Library()

# 获取平台信息
@register.simple_tag
def Get_PlatForm_Info(uid, pid):
    return PlatformUserInfo.objects.filter(platform_id=int(pid)).filter( user_id=int(uid))

@register.simple_tag
def Get_Company_Plat_Nums():
    return PlatformInfo.objects.filter(status=1).filter(belong=1).count()

@register.simple_tag
def Get_Others_Plat_Nums():
    return PlatformInfo.objects.filter(status=1).filter(belong=1).count()

