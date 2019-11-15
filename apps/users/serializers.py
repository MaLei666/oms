#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 20:57
# @file : serializers.py
# @software : PyCharm

from .models import *
from rest_framework import serializers

__all__=('UserSerializer',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = '__all__'
        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        validated_data['create_user']=self.context['request'].user.username
        validated_data['user_id_create']=self.context['request'].user.id
        obj = super(UserSerializer, self).create(validated_data=validated_data)
        obj.save()
        return obj

    # def update(self, instance, validated_data):
    #     instance.user_name=validated_data.get('user_name',instance.user_name)
    #     instance.mobile=validated_data.get('mobile',instance.mobile)
    #     instance.avatar=validated_data.get('avatar',instance.avatar)
    #     instance.gender=validated_data.get('gender',instance.gender)
    #     instance.comment=validated_data.get('comment',instance.comment)
    #     instance.status=validated_data.get('user_name',instance.status)
    #     instance.email=validated_data.get('email',instance.email)
    #     instance.is_staff=validated_data.get('is_staff',instance.is_staff)
    #     instance.update_user=validated_data.user.user_name
    #
    #     instance.save()
    #     return instance


class UserInfoSerializer(UserSerializer):
    class Meta:
        model=UserProfile
        fields = ['password', 'last_login', 'is_superuser', 'username', 'email', 'is_staff','date_joined','role',
                  'user_name','unit_id','unit_name','dept_id','dept_name','mobile','avatar','gender','create_user',
                  'create_time','update_user','update_time','comment','status','user_id_create']

