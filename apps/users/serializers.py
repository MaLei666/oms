#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 20:57
# @file : serializers.py
# @software : PyCharm

from .models import *
from rest_framework import serializers
from datetime import datetime as dt

__all__=('UserSerializer',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = ['id','password', 'last_login', 'username', 'email','role','user_name','unit_id','unit_name','dept_id',
                  'dept_name','mobile','gender','create_time','comment','status']
        read_only_fields = (
            'id','username','role','unit_id','dept_id'
        )

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj = super(UserSerializer, self).create(validated_data=validated_data)
        return obj


    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(UserSerializer,self).update(validated_data=validated_data,instance=instance)
        return obj



