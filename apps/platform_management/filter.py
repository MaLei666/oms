#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-15 11:48
# @file : filter.py
# @software : PyCharm

import django_filters
from .models import *

__all__=['platFilter','platUserFilter']

class platFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(method="name_filter")
    belong=django_filters.CharFilter(method="belong_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = platformInfo
        fields = ['name', 'belong','unit_name', 'dept_name', 'status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def belong_filter(queryset, value):
        return queryset.filter(belong=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)


class platUserFilter(django_filters.FilterSet):
    platform = django_filters.CharFilter(method="platform_filter")
    unit_name = django_filters.CharFilter(method="unit_name_filter")
    dept_name = django_filters.CharFilter(method="dept_name_filter")
    username=django_filters.CharFilter(method="username_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = platformUserInfo
        fields = ['platform','username','status']

    @staticmethod
    def platform_filter(queryset, value):
        return queryset.filter(platform__icontains=value)

    @staticmethod
    def username_filter(queryset, value):
        return queryset.filter(username__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)
