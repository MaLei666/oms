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

__all__=['docSerializer']

class docSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields = ['id', 'subject','tags_id','tags','content','belong','create_user','create_time','update_time',
                  'status','unit_id','unit_name','dept_id','dept_name']

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj=super(docSerializer, self).create(validated_data=validated_data)

        # 添加操作记录
        UserOperation(op_user = self.context['request'].user,
                      belong = 4,
                      status = 1,
                      op_num = obj.id,
                      operation = 1,
                      action = "新增文档[ %s ]" % (validated_data['subject']))
        return obj

    def update(self, instance, validated_data):
        instance.update_user=self.context['request'].user.username
        instance.update_time=dt.now()
        obj=super(docSerializer,self).update(validated_data=validated_data,instance=instance)

        UserOperation(op_user=self.context['request'].user,
                      belong=4,
                      status=1,
                      op_num=obj.id,
                      operation=2,
                      action="修改文档[ %s ]" % (instance.subject))
        return obj

    def delete(self,request,instance):
        UserOperation(op_user=request.user,
                      belong=2,
                      status=1,
                      op_num=instance.id,
                      operation=4,
                      action="删除文档：[ %s ]" % (instance.subject))
        return instance