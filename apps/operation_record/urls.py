"""
operation_record app
"""
from django.urls import path
from operation_record.apis.opera_api import *

__all__=['urlpatterns','app_name']

app_name = 'operation_record'

opera_list=operationView.as_view({
    'get': 'list',

})

urlpatterns = [
    path('record', opera_list, name='op_record'),

]


