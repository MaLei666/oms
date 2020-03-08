#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-15 11:48
# @file : filter.py
# @software : PyCharm

import django_filters
from .models import *

__all__=['docFilter']

class docFilter(django_filters.FilterSet):
    subject=django_filters.CharFilter(method="subject_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    tags = django_filters.CharFilter(method="tags_filter")
    belong = django_filters.CharFilter(method="belong_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = Document
        fields = ['subject', 'unit_name', 'dept_name', 'tags','belong','status']

    @staticmethod
    def subject_filter(queryset, value):
        return queryset.filter(subject__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def tags_filter(queryset, value):
        return queryset.filter(tags__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def belong_filter(queryset, value):
        return queryset.filter(belong__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)