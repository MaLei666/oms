# #!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# # -*- coding:utf-8 -*-
# # @author : MaLei
# # @datetime : 2019-11-12 21:11
# # @file : document_api.py
# # @software : PyCharm

from document_management.serializers import *
from ..filter import *
from utils.code_response import response_fomat
from ..models import *
######################################
# 第三方模块
######################################
from rest_framework import viewsets
from rest_framework.response import Response

__all__ = ['docViewSet']

class docViewSet(viewsets.ModelViewSet):
    serializer_class =docSerializer
    queryset = Document.objects.all().order_by('id')
    filter_class = docFilter
    lookup_url_kwarg = 'doc_id'
    code = response_fomat()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role < 3:
                return self.queryset.all.order_by('id')
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
                or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['doc_id']).unit_id) \
                or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['doc_id']).dept_id):
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.request_edit_succeed())
        else:
            return Response(self.code.no_permission())

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role < 3 \
                    or (request.user.role==3 and request.user.unit_id == self.queryset.get(id=self.kwargs['doc_id']).unit_id) \
                    or (request.user.role > 3 and request.user.dept_id == self.queryset.get(id=self.kwargs['doc_id']).dept_id):
                instance = self.get_object()
                docSerializer().delete(request, instance)
                self.perform_destroy(instance)
                return Response(self.code.request_delete_succeed())
            else:
                return Response(self.code.no_permission())
        except:
            return Response(self.code.internal_server_error())
