# from django.contrib import admin
from .models import *
import xadmin
# Register your models here.
xadmin.site.register(InspectDevInfo)
xadmin.site.register(InspectContentInfo)