#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : user_api.py
# @software : PyCharm

from users.serializers import *
from ..filter import *
from utils.code_response import responseFomat
from ..models import *

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from rest_framework.request import Request
from rest_framework import status,generics,viewsets,renderers
from rest_framework.decorators import action
from rest_framework.response import Response




__all__=['UserViewSet','unitViewSet','deptViewSet']


# Todo
# @csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all().order_by('id')
    filter_class=UserFilter
    lookup_url_kwarg = 'user_id'
    code = responseFomat()

    def create(self, request, *args, **kwargs):
        if request.user.role < request.data.get('role'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(self.code.requestAddSucceed())
        else:
            return Response(self.code.noPermission())

    # @action(methods=['PATCH'], detail=True)
    def partial_update(self, request, *args, **kwargs):
        if request.user.role < self.get_object().role or request.user.id==kwargs['user_id']:
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.requestEditSucceed())
        else:
            return Response(self.code.noPermission())


    def destroy(self, request, *args, **kwargs):
        if request.user.role < self.get_object().role:
            instance = self.get_object()
            UserSerializer().delete(request,instance)
            self.perform_destroy(instance)
            return Response(self.code.requestDeleteSucceed())
        else:
            return Response(self.code.noPermission())

class unitViewSet(viewsets.ModelViewSet):
    serializer_class =unitSerializer
    queryset = UserCompany.objects.all().order_by('id')
    filter_class = unitFilter
    lookup_url_kwarg = 'unit_id'
    code = responseFomat()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(self.code.requestAddSucceed())
        else:
            return Response(self.code.noPermission())

    # @action(methods=['PATCH'], detail=True)
    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or request.user.unit_id == kwargs['unit_id']:
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.requestEditSucceed())
        else:
            return Response(self.code.noPermission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3:
            instance = self.get_object()
            unitSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.requestDeleteSucceed())
        else:
            return Response(self.code.noPermission())

class deptViewSet(viewsets.ModelViewSet):
    serializer_class =deptSerializer
    queryset = UserDepartment.objects.all().order_by('id')
    filter_class = deptFilter
    lookup_url_kwarg = 'dept_id'
    code = responseFomat()

    def create(self, request, *args, **kwargs):
        if request.user.role < 4:
            try:
                self.queryset.get(unit_id=request.data['unit_id'], name=request.data['name'])
                return Response(self.code.duplicateData())
            except:
                request.data['unit_name'] = UserCompany.objects.get(id=request.data['unit_id']).name
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                return Response(self.code.requestAddSucceed())
        else:
            return Response(self.code.noPermission())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or request.user.unit_id==self.queryset.get(id=self.kwargs['dept_id']).unit_id \
                or request.user.dept_id==self.kwargs['dept_id']:
            try:
                self.queryset.get(unit_id=self.queryset.get(id=self.kwargs['dept_id']).unit_id,
                                   name=request.data['name'])
                return Response(self.code.duplicateData())


            except:
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.requestEditSucceed())
        else:
            return Response(self.code.noPermission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3 or request.user.unit_id==self.queryset.get(id=self.kwargs['dept_id']).unit_id:
            instance = self.get_object()
            deptSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.requestDeleteSucceed())
        else:
            return Response(self.code.noPermission())








