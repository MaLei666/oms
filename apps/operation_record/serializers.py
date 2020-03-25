#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 20:57
# @file : serializers.py
# @software : PyCharm
__all__=['operaSerializer']

from .models import UserOperationRecord
from rest_framework import serializers



class operaSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserOperationRecord
        fields=['id','user','username','user_name','role','unit_id','unit_name','dept_id',
                'dept_name','belong','operation','op_num','action','status','add_time']
