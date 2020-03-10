# from django.contrib import admin
from .models import UserOperationRecord
import xadmin
from xadmin.layout import Fieldset

class operaSetting(object):
    form_layout = (
        Fieldset('用户操作',
                 'username',
                 'user_name',
                 'role',
                 'unit_name',
                 'dept_name',
                 'belong',
                 'operation',
                 'op_num',
                 'action',
                 'status',
                 'add_time',
            ),
    )
    list_display = ['id','username','user_name','role','unit_name','dept_name','belong','operation',
                    'action', 'status', 'add_time']
    list_filter = ['status','belong','operation']
    search_fields = ['unit_name','dept_name','user_name']
    ordering = ['-add_time']

# Register your models here.
xadmin.site.register(UserOperationRecord,operaSetting)
