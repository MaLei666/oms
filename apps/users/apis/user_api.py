#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : user_api.py
# @software : PyCharm

from users.serializers import UserSerializer,deptSerializer,unitSerializer
from ..filter import *
from utils.code_response import responseFomat
from ..models import *
from django.contrib.auth.hashers import make_password

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from rest_framework.request import Request
from rest_framework import status,generics,viewsets,renderers,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken,APIView
from rest_framework.exceptions import PermissionDenied
__all__=['UserViewSet','unitViewSet','deptViewSet','userLogin']


# @csrf_exempt
class lsLogin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner==request.user

class unitViewSet(viewsets.ModelViewSet):
    serializer_class =unitSerializer
    queryset = UserCompany.objects.all().order_by('id')
    filter_class = unitFilter
    lookup_url_kwarg = 'unit_id'
    code = responseFomat()

    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role<3:
                return self.queryset
            else:
                return self.queryset.filter(id=user.unit_id)
        raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(self.code.requestAddSucceed(),status=status.HTTP_200_OK)
        else:
            return Response(self.code.noPermission())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                (request.user.unit_id == kwargs['unit_id'] and request.user.role==3):
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

    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role<3:
                return self.queryset
            elif user.role==3:
                return self.queryset.filter(unit_id=user.unit_id)
            else:
                return self.queryset.filter(id=user.dept_id)
        raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                (request.user.role==3 and request.data['unit_id']==request.user.unit_id):
            if self.queryset.filter(unit_id=request.data['unit_id'], name=request.data['name']):
                return Response(self.code.duplicateData())
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                return Response(self.code.requestAddSucceed())
        else:
            return Response(self.code.noPermission())

    def partial_update(self, request, *args, **kwargs):
        if request.user.role < 3 or \
                request.user.dept_id == self.kwargs['dept_id'] or \
                (request.user.role==3 and request.user.unit_id==self.queryset.get(id=self.kwargs['dept_id']).unit_id):
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
        if request.user.role < 3 or \
                (request.user.unit_id==self.queryset.get(id=self.kwargs['dept_id']).unit_id and request.user.role==3):
            instance = self.get_object()
            deptSerializer().delete(request, instance)
            self.perform_destroy(instance)
            return Response(self.code.requestDeleteSucceed())
        else:
            return Response(self.code.noPermission())


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all().order_by('id')
    filter_class=UserFilter
    lookup_url_kwarg = 'user_id'
    code = responseFomat()

    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role<3:
                return UserProfile.objects.filter(role__gte=user.role).order_by('id')
            elif user.role==3:
                return self.queryset.filter(unit_id=user.unit_id,role__gte=user.role)
            else:
                return self.queryset.filter(dept_id=user.dept_id,role__gte=user.role)
        raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        if request.user.role < request.data.get('role'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(self.code.requestAddSucceed())
        else:
            return Response(self.code.noPermission())

    def partial_update(self, request, *args, **kwargs):
        instance=self.get_object()
        if request.user.id==kwargs['user_id'] or \
                (request.user.role <3 and request.user.role< instance.role) or \
                (request.user.unit_id==instance.unit_id and request.user.role< instance.role) or \
                (request.user.dept_id==instance.dept_id and request.user.role< instance.role):
            kwargs['partial'] = True
            self.update(request, *args, **kwargs)
            return Response(self.code.requestEditSucceed())
        else:
            return Response(self.code.noPermission())


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if (request.user.role <3 and request.user.role< instance.role) or \
                (request.user.unit_id == instance.unit_id and request.user.role < instance.role) or \
                (request.user.dept_id == instance.dept_id and request.user.role < instance.role):
            UserSerializer().delete(request,instance)
            self.perform_destroy(instance)
            return Response(self.code.requestDeleteSucceed())
        else:
            return Response(self.code.noPermission())
# Todo
class userLogin(APIView):
    def post(self,request,*args,**kwargs):
        try:
            username=request.data.get('username')
            password=request.data.get('password')
            obj=UserProfile.objects.filter(username=username).first()
            if not obj:
                return Response(responseFomat().dataHandleFailed())
        except:
            return Response(responseFomat().dataHandleFailed())
        return Response(responseFomat().dataHandleSucceeded())





