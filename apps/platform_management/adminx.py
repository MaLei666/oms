# from django.contrib import admin
from .models import *
import xadmin
# Register your models here.
xadmin.site.register(PlatformInfo)
xadmin.site.register(PlatformUserInfo)