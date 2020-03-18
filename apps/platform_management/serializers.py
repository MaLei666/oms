#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 20:57
# @file : serializers.py
# @software : PyCharm

from .models import *
from rest_framework import serializers
from datetime import datetime as dt
from utils.commen_method import UserOperation

__all__=['platSerializer','platUserSerializer']

class platSerializer(serializers.ModelSerializer):
    class Meta:
        model=platformInfo
        fields = ['id', 'unit_id','unit_name','dept_id','dept_name','name','url','belong',
                  'create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(platSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 6,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增平台信息：[ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(platSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=6,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改平台信息：[ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=6,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除平台信息：[ %s ]" % instance.name)
        return instance


class platUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=platformUserInfo
        fields = ['id', 'platform_id', 'platform','username','password','create_user','create_time',
                  'update_time','comment','status','unit_id','unit_name','dept_id','dept_name',]

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(platUserSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增平台用户信息 [ %s:%s ]" % (validated_data['platform'],validated_data['username']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(platUserSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=6,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改平台用户信息：[ %s:%s ]" % (instance.platform,instance.username))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=6,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除平台用户信息 [ %s:%s ]" % (instance.platform,instance.username))
        return instance

