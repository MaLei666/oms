#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# -*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : user_api.py
# @software : PyCharm

from utils.code_response import response_fomat
from ..serializers import operaSerializer
from ..models import UserOperationRecord
######################################
# 第三方模块
######################################
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin

__all__ = ['operationView']


######################################
# 用户操作查询
######################################
class operationView(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = operaSerializer
    queryset=UserOperationRecord.objects.all().order_by('id')

    def get_queryset(self):
        try:
            user = self.request.user
            if user.is_authenticated:
                if user.role<3:
                    return self.queryset.filter(role__gte=user.role).order_by('-add_time')
                elif user.role==3:
                    return self.queryset.filter(unit_id=user.unit_id, role__gte=user.role).order_by('-add_time')
                elif user.role==4:
                    return self.queryset.filter(dept_id=user.dept_id, role__gte=user.role).order_by('-add_time')
                else:
                    return self.queryset.filter(user_id=user.id).order_by('-add_time')
            else:
                return Response(response_fomat().authenticat_failed())
        except:
            return Response(response_fomat().internal_server_error())











