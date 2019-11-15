#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : user_api.py
# @software : PyCharm

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from users.models import *
from users.serializers import UserSerializer,UserInfoSerializer
from ..filter import *

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from rest_framework.request import Request
from rest_framework import status,generics

# Todo
# @csrf_exempt
class UserlistApi(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    filter_class=UserFilter


# @csrf_exempt
class UserInfoApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserInfoSerializer
    lookup_url_kwarg = 'user_id'

class UserCreateApi(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        response = super(UserCreateApi, self).create(request, *args, **kwargs)
        return response



