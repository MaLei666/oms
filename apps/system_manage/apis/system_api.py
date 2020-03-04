# #!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# # -*- coding:utf-8 -*-
# # @author : MaLei
# # @datetime : 2019-11-12 21:11
# # @file : system_api.py
# # @software : PyCharm

from system_manage.serializers import *
from ..filter import *
from utils.code_response import response_fomat
from ..models import *
######################################
# 第三方模块
######################################
from rest_framework import viewsets
from rest_framework.response import Response

__all__ = ['portViewSet', 'domainViewSet', 'domainResvViewSet','dataDictViewSet',]

class portViewSet(viewsets.ModelViewSet):
    serializer_class =portSerializer
    queryset = portToPortInfo.objects.all().order_by('id')
    filter_class = portFilter
    lookup_url_kwarg = 'port_id'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return self.queryset
        else:
            return self.code.authenticat_failed()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3 or request.data['unit_id'] == request.user.unit_id:
            if self.queryset.filter(ip_out=request.data['ip_out'], port_out=request.data['port_out']):
                return Response(self.code.duplicate_data())
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=True):
                return Response(self.code.data_illegal())
            self.perform_create(serializer)
            return Response(self.code.request_add_succeed())
        else:
            return Response(self.code.no_permission())


    def partial_update(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 or \
                    request.user.unit_id == self.queryset.get(id=self.kwargs['port_id']).unit_id:
                kwargs['partial'] = True
                self.update(request, *args, **kwargs)
                return Response(self.code.request_edit_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 or \
                    request.user.unit_id == self.queryset.get(id=self.kwargs['port_id']).unit_id:
                instance = self.get_object()
                portSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


class domainViewSet(viewsets.ModelViewSet):
    serializer_class = domainNameSerializer
    queryset = domainNameInfo.objects.all().order_by('id')
    filter_class = domainFilter
    lookup_url_kwarg = 'domain_id'
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
                request.user.unit_id == self.queryset.get(id=self.kwargs['domain_id']).unit_id:
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['domain_id']).unit_id:
            instance = self.get_object()
            domainNameSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        else:
            return Response(self.code.no_permission())


class domainResvViewSet(viewsets.ModelViewSet):
    serializer_class = domainResolveSerializer
    queryset = domainNameResolveInfo.objects.all().order_by('id')
    lookup_url_kwarg = 'domain_resv_id'
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
            if self.queryset.filter(domain_name_id=request.data['domain_name_id'],
                                    ip=request.data['ip']):
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
                request.user.unit_id == self.queryset.get(id=self.kwargs['domain_resv_id']).unit_id:
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.unit_id == self.queryset.get(id=self.kwargs['domain_resv_id']).unit_id:
            instance = self.get_object()
            domainResolveSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.request_delete_succeed())
        else:
            return Response(self.code.no_permission())


class dataDictViewSet(viewsets.ModelViewSet):
    serializer_class = dataDictSerializer
    queryset = dataDictInfo.objects.all().order_by('id')
    filter_class = dataDictFilter
    lookup_url_kwarg = 'dict_id'
    code = response_fomat()

    def get_queryset(self):
        try:
            user = self.request.user
            if user.is_authenticated and user.role < 2:
                    return self.queryset
            else:
                return Response(self.code.authenticat_failed())
        except:
            return Response(self.code.internal_server_error())

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role<2:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                return Response(self.code.request_add_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())


    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 2:
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 2:
                instance = self.get_object()
                dataDictSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())

