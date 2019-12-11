#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : user_api.py
# @software : PyCharm

from users.serializers import UserSerializer
from ..filter import *
from utils.code_response import responseFomat

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from rest_framework.request import Request
from rest_framework import status,generics,viewsets,renderers
from rest_framework.decorators import action
from rest_framework.response import Response



__all__=['UserViewSet']

code=responseFomat()
# Todo
# @csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all().order_by('id')
    filter_class=UserFilter
    lookup_url_kwarg = 'user_id'

    # @action(methods=['POST'], detail=False)
    def perform_create(self, serializer):
        serializer.save()

    # @action(methods=['PATCH'], detail=True)
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


    def delete(self, request,user_id):
        self.destroy(request,user_id)
        return Response(code.dataHandleSucceeded())










