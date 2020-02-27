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

__all__=['systemSerializer','projectSerializer','useSerializer','idcSerializer','rackSerializer',
         'hostSerializer','hostServiceSerializer','databaseDBSerializer','databaseSerializer']

class systemSerializer(serializers.ModelSerializer):
    class Meta:
        model=operatingSystemInfo
        fields = ['id', 'name','version', 'bit','user_id_create','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(systemSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增操作系统 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(systemSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改操作系统 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除操作系统 [ %s ]" % instance.name)
        return instance

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model=projectInfo
        fields = ['id', 'name','op_user','run_env','unit_name','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(projectSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增项目 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(projectSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改项目 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name=request.user.user_name,
                      role=request.user.role,
                      unit_id=request.user.unit_id,
                      unit_name=request.user.unit_name,
                      dept_id=request.user.dept_id,
                      dept_name=request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除项目 [ %s ]" % instance.name)
        return instance

class useSerializer(serializers.ModelSerializer):
    class Meta:
        model=useInfo
        fields = ['id', 'name','create_user','create_time','update_time','comment','status']
        read_only_fields = ('id',)

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(useSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增用途 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(useSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改用途 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name=request.user.user_name,
                      role=request.user.role,
                      unit_id=request.user.unit_id,
                      unit_name=request.user.unit_name,
                      dept_id=request.user.dept_id,
                      dept_name=request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除用途 [ %s ]" % instance.name)
        return instance

class idcSerializer(serializers.ModelSerializer):
    class Meta:
        model=idcInfo
        fields = ['id', 'name','unit_name','isp','line','bandwidth','racks','address','connect',
                  'connect_phone','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(idcSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增机房 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(idcSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改机房 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除机房 [ %s ]" % instance.name)
        return instance

class rackSerializer(serializers.ModelSerializer):
    class Meta:
        model=rackInfo
        fields = ['id', 'name','unit_name','idc_name','number','height','power','create_user',
                  'create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(rackSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增机柜 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(rackSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改机柜 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除机柜 [ %s ]" % instance.name)
        return instance

class hostSerializer(serializers.ModelSerializer):
    class Meta:
        model=hostInfo
        fields = ['id', 'hostname', 'in_ip', 'out_ip','system','unit_name','dept_name','idc_name',
                  'rack_name','address','disk','memory','network','ssh_port','root_ssh','use',
                  'project','create_user','create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(hostSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增主机 [ %s ]：[ %s ]" % (validated_data['hostname'],
                                                       validated_data['in_ip']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(hostSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改主机 [ %s ]：[ %s ]" % (instance.hostname,instance.in_ip))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除主机 [ %s ]：[ %s ]" % (instance.hostname,instance.in_ip))
        return instance

class hostServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=hostServiceInfo
        fields = ['id', 'hostname','unit_name','dept_name','name','version','listen_user','listen_port',
                  'ins_path','log_path','backup_path','start_cmd','create_user','create_time',
                  'update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(hostServiceSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增服务信息 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(hostServiceSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改服务信息 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除服务信息 [ %s ]" % instance.name)
        return instance

class databaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=databaseInfo
        fields = ['id', 'hostname', 'unit_name','dept_name','db_name','db_version','create_user',
                  'create_time','update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(databaseSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增数据库服务信息 [ %s ]" % validated_data['db_name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(databaseSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改数据库服务信息 [ %s ]" % instance.db_name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除数据库服务信息 [ %s ]" % instance.db_name)
        return instance

class databaseDBSerializer(serializers.ModelSerializer):
    class Meta:
        model=databaseDBInfo
        fields = ['id','unit_name','dept_name','name','use','create_user','create_time',
                  'update_time','comment','status']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(databaseDBSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong = 1,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增数据库 [ %s ]" % validated_data['name'])
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(databaseDBSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      username=self.context['request'].user.username,
                      user_name=self.context['request'].user.user_name,
                      role=self.context['request'].user.role,
                      unit_id=self.context['request'].user.unit_id,
                      unit_name=self.context['request'].user.unit_name,
                      dept_id=self.context['request'].user.dept_id,
                      dept_name=self.context['request'].user.dept_name,
                      belong=1,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改数据库 [ %s ]" % instance.name)
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      username=request.user.username,
                      user_name = request.user.user_name,
                      role = request.user.role,
                      unit_id = request.user.unit_id,
                      unit_name = request.user.unit_name,
                      dept_id = request.user.dept_id,
                      dept_name = request.user.dept_name,
                      belong=1,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除数据库 [ %s ]" % instance.name)
        return instance