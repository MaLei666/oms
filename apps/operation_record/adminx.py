# from django.contrib import admin
from .models import UserOperationRecord
import xadmin
# Register your models here.
xadmin.site.register(UserOperationRecord)