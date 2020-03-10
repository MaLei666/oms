import xadmin
from xadmin.layout import Fieldset
######################################
# 自己写的模块
######################################
from .models import *

class docSetting(object):
    # fieldsets=()
    form_layout = (
        Fieldset('文档详情',
                'unit_name',
                'dept_name',
                'subject',
                'tags',
                'content',
                'belong',
                'status',
            ),
        # Fieldset(None,
        #          )
    )
    list_display = ['id','unit_name','dept_name','subject','tags','belong','status', 'create_time']
    list_filter = ['unit_name', 'dept_name', 'subject', 'tags','belong','status']
    search_fields = ['unit_name','dept_name','subject', 'tags', 'belong']
    ordering = ['-create_time']


# Register your models here.
xadmin.site.register(Document,docSetting)