#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-15 11:48
# @file : filter.py
# @software : PyCharm

import django_filters
from django.db.models import Q
from .models import *

__all__=['UserFilter','unitFilter','deptFilter']

class UserFilter(django_filters.FilterSet):
    role=django_filters.CharFilter(method="role_filter")
    unit_id=django_filters.CharFilter(method="unit_id_filter")
    dept_id=django_filters.CharFilter(method="dept_id_filter")
    mobile = django_filters.CharFilter(method="mobile_filter")
    username = django_filters.CharFilter(method="username_filter")
    user_name=django_filters.CharFilter(method="user_name_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = UserProfile
        fields = ['role', 'unit_id', 'dept_id', 'mobile', 'username','user_name','status']

    @staticmethod
    def role_filter(queryset, value):
        return queryset.filter(role__icontains=value)

    @staticmethod
    def unit_id_filter(queryset, value):
        return queryset.filter(unit_id__icontains=value)

    @staticmethod
    def dept_id_filter(queryset, value):
        return queryset.filter(dept_id__icontains=value)

    @staticmethod
    def mobile_filter(queryset, value):
        return queryset.filter(mobile__icontains=value)

    @staticmethod
    def username_filter(queryset, value):
        return queryset.filter(username__icontains=value)

    @staticmethod
    def user_name_filter(queryset, value):
        return queryset.filter(user_name__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class unitFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(method="name_filter")
    connect = django_filters.CharFilter(method="connect_filter")
    connect_phone = django_filters.CharFilter(method="connect_phone_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = UserCompany
        fields = ['name', 'connect', 'connect_phone', 'status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def connect_filter(queryset, value):
        return queryset.filter(connect__icontains=value)

    @staticmethod
    def connect_phone_filter(queryset, value):
        return queryset.filter(connect_phone__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class deptFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(method="name_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    connect = django_filters.CharFilter(method="connect_filter")
    connect_phone = django_filters.CharFilter(method="connect_phone_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = UserDepartment
        fields = ['name', 'unit_name','connect', 'connect_phone', 'status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def connect_filter(queryset, value):
        return queryset.filter(connect__icontains=value)

    @staticmethod
    def connect_phone_filter(queryset, value):
        return queryset.filter(connect_phone__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)