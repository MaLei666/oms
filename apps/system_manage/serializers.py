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

__all__=['portSerializer','domainNameSerializer','domainResolveSerializer','dataDictSerializer']

class portSerializer(serializers.ModelSerializer):
    class Meta:
        model=portToPortInfo
        fields = ['id', 'unit_id','unit_name','dept_id','dept_name','ip_out','port_out','ip_in','port_in','use',
                  'create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(portSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 2,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增 [ %s:%s ] 映射：[ %s:%s ]" % (validated_data['ip_out'],validated_data['port_out'],
                                                              validated_data['ip_in'],validated_data['port_in']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(portSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改[ %s:%s ] 映射：[ %s:%s ]" % (instance.ip_out,instance.port_out,
                                                           instance.ip_in,instance.port_in))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除[ %s:%s ] 映射：[ %s:%s ]" % (instance.ip_out,instance.port_out,
                                                           instance.ip_in,instance.port_in))
        return instance


class domainNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=domainNameInfo
        fields = ['id', 'name', 'unit_id','unit_name','dept_id','dept_name','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(domainNameSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增域名信息 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(domainNameSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改域名信息 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除域名信息 [ %s ]" % instance.name)
        return instance


class domainResolveSerializer(serializers.ModelSerializer):
    class Meta:
        model=domainNameResolveInfo
        fields = ['id', 'name','domain_name', 'unit_id','unit_name','dept_id','dept_name','ip','create_user','create_time',
                  'update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(domainResolveSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增域名解析 [ %s ]——[ %s ]" % (validated_data['domain_name'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(domainResolveSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改域名解析 [ %s ]——[ %s ]" % (instance.domain_name,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除域名解析 [ %s ]——[ %s ]" % (instance.domain_name,instance.name))
        return instance


class dataDictSerializer(serializers.ModelSerializer):
    class Meta:
        model=dataDictInfo
        fields = ['id', 'name','value','type','description', 'sort','parent_id','create_user',
                  'create_time','update_time','comment']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(dataDictSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增数据字典 [ %s ]——[ %s ]" %(validated_data['name'],validated_data['value']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(dataDictSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=2,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改数据字典 [ %s ]——[ %s ]" % (instance.name,instance.value))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除数据字典 [ %s ]——[ %s ]" % (instance.name,instance.value))
        return instance

