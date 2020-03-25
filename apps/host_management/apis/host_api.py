#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# -*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : host_api.py
# @software : PyCharm

from host_management.serializers import *
from ..filter import *
from utils.code_response import response_fomat
from ..models import *
######################################
# 第三方模块
######################################
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin


__all__ = ['osViewSet', 'projectViewSet', 'useViewSet','idcViewSet','rackViewSet','hostViewSet',
           'hostserviceViewSet','databaseViewSet','databaseDBViewSet',]


class osViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class =systemSerializer
    queryset = operatSystemInfo.objects.all().order_by('id')
    filter_class = systemFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return self.queryset
        else:
            return self.code.authenticat_failed()

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(self.code.request_add_succeed())
        except:
            return Response(self.code.internal_server_error())

    def partial_update(self, request, *args, **kwargs):
        try:
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
        except:
            return Response(self.code.internal_server_error())

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            systemSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        except:
            return Response(self.code.internal_server_error())


class projectViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = projectSerializer
    queryset = projectInfo.objects.all().order_by('id')
    filter_class = projectFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role < 3:
                return self.queryset
            else:
                return self.queryset.filter(unit_id=user.unit_id)
        else:
            return self.code.authenticat_failed()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3 or request.data['unit_id'] == request.user.unit_id:
            if self.queryset.filter(unit_id=request.data['unit_id'], name=request.data['name']):
                return Response(self.code.duplicate_data())
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=True):
                return Response(self.code.data_illegal())
            self.perform_create(serializer)
            return Response(self.code.request_add_succeed())
        else:
            return Response(self.code.no_permission())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id:
            try:
                self.queryset.get(unit_id=self.queryset.get(id=self.kwargs['pk']).unit_id,
                                  name=request.data['name'])
                return Response(self.code.duplicate_data())
            except:
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id:
            instance = self.get_object()
            projectSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        else:
            return Response(self.code.no_permission())


class useViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = useSerializer
    queryset = useInfo.objects.all().order_by('id')
    filter_class = useFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(self.code.request_add_succeed())
        except:
            return Response(self.code.internal_server_error())

    def partial_update(self, request, *args, **kwargs):
        try:
            self.queryset.get(name=request.data['name'])
            return Response(self.code.duplicate_data())
        except:
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())


    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            useSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        except:
            return Response(self.code.internal_server_error())


class idcViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = idcSerializer
    queryset = idcInfo.objects.all().order_by('id')
    filter_class = idcFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role < 3:
                return self.queryset
            else:
                return self.queryset.filter(unit_id=user.unit_id)
        else:
            return self.code.authenticat_failed()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3 or request.data['unit_id'] == request.user.unit_id:
            if self.queryset.filter(unit_id=request.data['unit_id'], name=request.data['name']):
                return Response(self.code.duplicate_data())
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=True):
                return Response(self.code.data_illegal())
            self.perform_create(serializer)
            return Response(self.code.request_add_succeed())
        else:
            return Response(self.code.no_permission())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id:
            try:
                self.queryset.get(unit_id=self.queryset.get(id=self.kwargs['pk']).unit_id,
                                  name=request.data['name'])
                return Response(self.code.duplicate_data())
            except:
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id:
            instance = self.get_object()
            idcSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        else:
            return Response(self.code.no_permission())


class rackViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = rackSerializer
    queryset = rackInfo.objects.all().order_by('id')
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role < 3:
                return self.queryset
            else:
                return self.queryset.filter(unit_id=user.unit_id)
        else:
            return self.code.authenticat_failed()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3 or request.data['unit_id'] == request.user.unit_id:
            if self.queryset.filter(unit_id=request.data['unit_id'], name=request.data['name']):
                return Response(self.code.duplicate_data())
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=True):
                return Response(self.code.data_illegal())
            self.perform_create(serializer)
            return Response(self.code.request_add_succeed())
        else:
            return Response(self.code.no_permission())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id:
            try:
                self.queryset.get(unit_id=self.queryset.get(id=self.kwargs['pk']).unit_id,
                                  name=request.data['name'])
                return Response(self.code.duplicate_data())
            except:
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id:
            instance = self.get_object()
            rackSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        else:
            return Response(self.code.no_permission())


class hostViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = hostSerializer
    queryset = hostInfo.objects.all().order_by('id')
    filter_class = hostFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        try:
            user = self.request.user
            if user.is_authenticated:
                if user.role < 3:
                    return self.queryset
                elif user.role == 3:
                    return self.queryset.filter(unit_id=user.unit_id)
                else:
                    return self.queryset.filter(dept_id=user.dept_id)
            else:
                return Response(self.code.authenticat_failed())
        except:
            return Response(self.code.internal_server_error())

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
                or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                instance = self.get_object()
                hostSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


class hostserviceViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = hostServiceSerializer
    queryset = hostServiceInfo.objects.all().order_by('id')
    filter_class = hostServiceFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        try:
            user = self.request.user
            if user.is_authenticated:
                if user.role < 3:
                    return self.queryset
                elif user.role == 3:
                    return self.queryset.filter(unit_id=user.unit_id)
                else:
                    return self.queryset.filter(dept_id=user.dept_id)
            else:
                return Response(self.code.authenticat_failed())
        except:
            return Response(self.code.internal_server_error())

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
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                instance = self.get_object()
                hostServiceSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


class databaseViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = databaseSerializer
    queryset = databaseInfo.objects.all().order_by('id')
    filter_class = databaseFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        try:
            user = self.request.user
            if user.is_authenticated:
                if user.role < 3:
                    return self.queryset
                elif user.role == 3:
                    return self.queryset.filter(unit_id=user.unit_id)
                else:
                    return self.queryset.filter(dept_id=user.dept_id)
            else:
                return Response(self.code.authenticat_failed())
        except:
            return Response(self.code.internal_server_error())

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
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                instance = self.get_object()
                databaseSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


class databaseDBViewSet(CacheResponseMixin,viewsets.ModelViewSet):
    serializer_class = databaseDBSerializer
    queryset = databaseDBInfo.objects.all().order_by('id')
    filter_class = databaseDBFilter
    lookup_url_kwarg = 'pk'
    code = response_fomat()

    def get_queryset(self):
        try:
            user = self.request.user
            if user.is_authenticated:
                if user.role < 3:
                    return self.queryset
                elif user.role == 3:
                    return self.queryset.filter(unit_id=user.unit_id)
                else:
                    return self.queryset.filter(dept_id=user.dept_id)
            else:
                return Response(self.code.authenticat_failed())
        except:
            return Response(self.code.internal_server_error())

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
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['pk']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['pk']).dept_id):
                instance = self.get_object()
                databaseDBSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


# ########################################################################################################################
# ## wessh主机视图
# ########################################################################################################################
# class WebSSHView(LoginStatusCheck, View):
#     def post(self, request, pk):
#         host = hostInfo.objects.get(id=int(pk))
#         ret = {}
#         try:
#             if host.out_ip:
#                 ip = host.out_ip
#             else:
#                 ip = host.in_ip
#
#             port = host.ssh_port
#
#             username = host.admin_user
#             password = host.admin_pass
#
#             ret = {"ip": ip, 'port': port, "username": username, 'password': password, "static": True}
#         except Exception as e:
#             ret['status'] = False
#             ret['error'] = '请求错误,{}'.format(e)
#         finally:
#             return HttpResponse(json.dumps(ret))


