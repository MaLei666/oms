#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020-03-18 21:45
# @file : plat_api.py
# @software : PyCharm

from platform_management.serializers import *
from ..filter import *
from utils.code_response import response_fomat
from ..models import *
######################################
# 第三方模块
######################################
from rest_framework import viewsets
from rest_framework.response import Response

__all__ = ['platViewSet', 'platUserViewSet']

class platViewSet(viewsets.ModelViewSet):
    serializer_class =platSerializer
    queryset = platformInfo.objects.all().order_by('id')
    filter_class = platFilter
    lookup_url_kwarg = 'plat_id'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role < 3:
                return self.queryset.filter(role__gte=user.role).order_by('id')
            elif user.role == 3:
                return self.queryset.filter(unit_id=user.unit_id)
            else:
                return self.queryset.filter(dept_id=user.dept_id, unit_id=user.unit_id)
        return Response(self.code.authenticat_failed())

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role<3 \
                    or (request.user.role==3 and request.user.unit_id == request.data['unit_id']) \
                    or (request.user.role>3 and request.user.dept_id == request.data['dept_id']):
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    return Response(self.code.request_add_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 \
                or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['plat_id']).unit_id) \
                or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['plat_id']).dept_id):
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['plat_id']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['plat_id']).dept_id):
                instance = self.get_object()
                platSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


class platUserViewSet(viewsets.ModelViewSet):
    serializer_class =platUserSerializer
    queryset = platformUserInfo.objects.all().order_by('id')
    filter_class = platUserFilter
    lookup_url_kwarg = 'platuser_id'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role < 3:
                return self.queryset.all().order_by('id')
            elif user.role == 3:
                return self.queryset.filter(unit_id=user.unit_id)
            else:
                return self.queryset.filter(dept_id=user.dept_id, unit_id=user.unit_id)
        return Response(self.code.authenticat_failed())

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role<3 \
                    or (request.user.role==3 and request.user.unit_id == request.data['unit_id']) \
                    or (request.user.role==4 and request.user.dept_id == request.data['dept_id']):
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    return Response(self.code.request_add_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 \
                or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['platuser_id']).unit_id) \
                or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['platuser_id']).dept_id):
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['platuser_id']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['platuser_id']).dept_id):
                instance = self.get_object()
                platUserSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())