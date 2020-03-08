#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-15 11:48
# @file : filter.py
# @software : PyCharm

import django_filters
from .models import *

__all__=['portFilter','domainFilter','domainResolveFilter','dataDictFilter']

class portFilter(django_filters.FilterSet):
    ip_in=django_filters.CharFilter(method="ip_in_filter")
    ip_out=django_filters.CharFilter(method="ip_out_filter")
    port_out=django_filters.CharFilter(method="port_out_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    port_in=django_filters.CharFilter(method="port_in_filter")
    use=django_filters.CharFilter(method="use_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = portToPortInfo
        fields = ['ip_in', 'ip_out','port_out','unit_name', 'dept_name', 'port_in','use','status']

    @staticmethod
    def ip_in_filter(queryset, value):
        return queryset.filter(ip_in__icontains=value)

    @staticmethod
    def ip_out_filter(queryset, value):
        return queryset.filter(ip_out__icontains=value)

    @staticmethod
    def port_out_filter(queryset, value):
        return queryset.filter(port_out__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def port_in_filter(queryset, value):
        return queryset.filter(port_in__icontains=value)

    @staticmethod
    def use_filter(queryset, value):
        return queryset.filter(use__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)


class domainFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = domainNameInfo
        fields = ['name','unit_name', 'dept_name','status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class domainResolveFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")
    domain_name=django_filters.CharFilter(method="domain_name_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    ip=django_filters.CharFilter(method="ip_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = domainNameResolveInfo
        fields = ['name', 'domain_name','unit_name', 'dept_name', 'ip','status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def domain_name_filter(queryset, value):
        return queryset.filter(domain_name__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def ip_filter(queryset, value):
        return queryset.filter(ip__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)


class dataDictFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")
    value=django_filters.CharFilter(method="value_filter")
    type=django_filters.CharFilter(method="type_filter")

    class Meta:
        model = domainNameResolveInfo
        fields = ['name', 'value','type']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def value_filter(queryset, value):
        return queryset.filter(value=value)

    @staticmethod
    def type_filter(queryset, value):
        return queryset.filter(type=value)
