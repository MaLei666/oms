#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 20:57
# @file : serializers.py
# @software : PyCharm

from .models import *
from rest_framework import serializers
from datetime import datetime as dt
from django.contrib.auth.hashers import make_password
from utils.commen_method import UserOperation
__all__=['UserSerializer','unitSerializer','deptSerializer','loginSerializer']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=userProfile
        fields = ['id', 'last_login', 'username', 'email','role','user_name','unit_id','unit_name','dept_id',
                  'dept_name','position','mobile','gender','create_time','update_time','comment','status']


    def create(self, validated_data):
        validated_data['password']=make_password(self.context['request'].data['password'])
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(UserSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 2,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增用户 [ %s ]" % validated_data['user_name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(UserSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改用户 [ %s ]" % instance.user_name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除用户 [ %s ]" % instance.user_name)
        return instance


class unitSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserCompany
        fields = ['id', 'name','connect','connect_phone','address','create_user','create_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(unitSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 2,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增单位 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(unitSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改单位 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除单位 [ %s ]" % instance.name)
        return instance

class deptSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDepartment
        fields = ['id', 'name','unit_id','unit_name','connect','connect_phone','create_user','create_time','comment','status']

    def create(self, validated_data):
        validated_data['unit_id']=self.context['request'].data['unit_id']
        validated_data['unit_name']=UserCompany.objects.get(id=validated_data['unit_id']).name
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(deptSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 2,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[%s]单位新增部门 [ %s ]" % (validated_data['unit_name'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(deptSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[%s]修改部门 [ %s ]" % (instance.unit_name,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[%s]删除部门 [ %s ]" % (instance.unit_name,instance.name))
        return instance

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLoginInfo
        fields=['id','action','user','username','user_name','role','unit_id','unit_name','dept_id',
                'dept_name','agent','ip','address','add_time']

        def create(self, validated_data):
            validated_data['unit_id'] = self.user.unit_id
            validated_data['unit_name'] = UserCompany.objects.get(id=validated_data['unit_id']).name
            validated_data['create_user'] = self.context['request'].user.username
            validated_data['user_id_create'] = self.context['request'].user.id
            obj = super(loginSerializer, self).create(validated_data=validated_data)

            # 添加操作记录
            UserOperation(op_user=self.context['request'].user,
                          belong=2,
                          status=1,
                          op_num=obj.id,
                          operation=1,
                          action="[%s]单位新增部门 [ %s ]" % (validated_data['unit_name'], validated_data['name']))

