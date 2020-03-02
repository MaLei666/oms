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
from django.contrib.auth.hashers import make_password


__all__=['systemSerializer','projectSerializer','useSerializer','idcSerializer','rackSerializer',
         'hostSerializer','hostServiceSerializer','databaseDBSerializer','databaseSerializer']

class systemSerializer(serializers.ModelSerializer):
    class Meta:
        model=operatSystemInfo
        fields = ['id', 'name','version', 'bit','create_user','create_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(systemSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增操作系统-[ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(systemSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改操作系统-[ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除操作系统-[ %s ]" % instance.name)
        return instance

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model=projectInfo
        fields = ['id', 'name','op_user','run_env','unit_id','unit_name','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(projectSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-新增项目-[ %s ]" % (validated_data['unit_name'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(projectSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-修改项目-[ %s ]" % (instance.unit_name,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-删除项目-[ %s ]" % (instance.unit_name,instance.name))
        return instance

class useSerializer(serializers.ModelSerializer):
    class Meta:
        model=useInfo
        fields = ['id', 'name','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(useSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增用途-[ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(useSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改用途-[ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除用途-[ %s ]" % instance.name)
        return instance

class idcSerializer(serializers.ModelSerializer):
    class Meta:
        model=idcInfo
        fields = ['id', 'name','unit_id','unit_name','isp','line','bandwidth','racks','address','connect',
                  'connect_phone','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(idcSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-新增机房-[ %s ]" % (validated_data['unit_name'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(idcSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-修改机房-[ %s ]" % (instance.unit_name,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-删除机房-[ %s ]" % (instance.unit_name,instance.name))
        return instance

class rackSerializer(serializers.ModelSerializer):
    class Meta:
        model=rackInfo
        fields = ['id', 'name','unit_id','unit_name','dept_id','dept_name','idc_id','idc_name','number',
                  'height','power','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(rackSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-[ %s ]-新增机柜-[ %s ]" %
                               (validated_data['unit_name'],validated_data['idc_name'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(rackSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-[ %s ]修改机柜-[ %s ]" % (instance.unit_name,instance.idc_name,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-[ %s ]删除机柜-[ %s ]" % (instance.unit_name,instance.idc_name,instance.name))
        return instance

class hostSerializer(serializers.ModelSerializer):
    class Meta:
        model=hostInfo
        fields = ['id', 'hostname', 'in_ip', 'out_ip','system_id','system','unit_id','unit_name','dept_id','dept_name',
                  'idc_id','idc_name','rack_id','rack_name','address','disk','memory','network','ssh_port','root_ssh',
                  'use_id','use','project_id','project','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        validated_data['admin_user'] = self.context['request'].data['admin_user']
        validated_data['admin_pass'] = make_password(self.context['request'].data['admin_pass'])
        obj=super(hostSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-[ %s ]新增主机-[ %s ]" % (validated_data['unit_name'],validated_data['dept_name'],
                                                             validated_data['in_ip']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(hostSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-[ %s ]修改主机-[ %s ]" % (instance.unit_name,instance.dept_name,instance.in_ip))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-[ %s ]删除主机-[ %s ]" % (instance.unit_name,instance.dept_name,instance.in_ip))
        return instance

class hostServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=hostServiceInfo
        fields = ['id','host_id','hostname','unit_id','unit_name','dept_id','dept_name','name','version','listen_user',
                  'listen_port','ins_path','log_path','backup_path','start_cmd','create_user','create_time',
                  'update_time','comment','status','in_ip','out_ip']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(hostServiceSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-新增服务信息-[ %s ]" % (validated_data['in_ip'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(hostServiceSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-修改服务信息-[ %s ]" % (instance.in_ip,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-删除服务信息-[ %s ]" % (instance.in_ip,instance.name))
        return instance

class databaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=databaseInfo
        fields = ['id','host_id','hostname', 'unit_id','unit_name','dept_id','dept_name','db_name','db_version',
                  'create_user','create_time','update_time','comment','status',]

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        validated_data['db_admin_user']=self.context['request'].data['db_admin_user']
        validated_data['db_admin_pass']=make_password(self.context['request'].data['db_admin_pass'])
        obj=super(databaseSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-[ %s ]新增数据库服务信息-[ %s ]" % (validated_data['unit_name'],
                                                                  validated_data['dept_name'],validated_data['db_name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(databaseSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-[ %s ]修改数据库服务信息-[ %s ]" % (instance.unit_name,instance.dept_name,instance.db_name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-[ %s ]删除数据库服务信息-[ %s ]" % (instance.unit_name,instance.dept_name,instance.db_name))
        return instance

class databaseDBSerializer(serializers.ModelSerializer):
    class Meta:
        model=databaseDBInfo
        fields = ['id','db_id','db_name','unit_id','unit_name','dept_id','dept_name','name','use','create_user',
                  'create_time','update_time','comment','status','host_id','hostname']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(databaseDBSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "[ %s ]-新增数据库-[ %s ]" % (validated_data['db_name'],validated_data['name']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(databaseDBSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="[ %s ]-修改数据库-[ %s ]" % (instance.db_name,instance.name))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="[ %s ]-删除数据库-[ %s ]" % (instance.db_name,instance.name))
        return instance