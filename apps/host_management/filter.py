#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-15 11:48
# @file : filter.py
# @software : PyCharm

import django_filters
from .models import *

__all__=['systemFilter','projectFilter','useFilter','idcFilter','hostFilter','hostServiceFilter',
         'databaseFilter','databaseDBFilter']

class systemFilter(django_filters.FilterSet):
    version=django_filters.CharFilter(method="version_filter")
    bit=django_filters.CharFilter(method="bit_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = operatSystemInfo
        fields = ['version', 'bit', 'status']

    @staticmethod
    def version_filter(queryset, value):
        return queryset.filter(version__icontains=value)

    @staticmethod
    def bit_filter(queryset, value):
        return queryset.filter(bit__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class projectFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(method="name_filter")
    run_env = django_filters.CharFilter(method="run_env_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = projectInfo
        fields = ['name', 'run_env', 'status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def run_env_filter(queryset, value):
        return queryset.filter(run_env__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class useFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(method="name_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = useInfo
        fields = ['name', 'status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class idcFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(method="name_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    isp = django_filters.CharFilter(method="isp_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = idcInfo
        fields = ['name', 'unit_name', 'dept_name', 'isp','status']

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
    def isp_filter(queryset, value):
        return queryset.filter(isp__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)


class hostFilter(django_filters.FilterSet):
    in_ip=django_filters.CharFilter(method="in_ip_filter")
    out_ip=django_filters.CharFilter(method="out_ip_filter")
    system=django_filters.CharFilter(method="system_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    idc_id=django_filters.CharFilter(method="idc_id_filter")
    rack_id=django_filters.CharFilter(method="rack_id_filter")
    disk=django_filters.CharFilter(method="disk_filter")
    memory=django_filters.CharFilter(method="memory_filter")
    use=django_filters.CharFilter(method="use_filter")
    project = django_filters.CharFilter(method="project_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = hostInfo
        fields = ['in_ip', 'out_ip','system','unit_name', 'dept_name', 'idc_id', 'rack_id',
                  'disk','memory','use','project','status']

    @staticmethod
    def in_ip_filter(queryset, value):
        return queryset.filter(in_ip__icontains=value)

    @staticmethod
    def out_ip_filter(queryset, value):
        return queryset.filter(out_ip__icontains=value)

    @staticmethod
    def system_filter(queryset, value):
        return queryset.filter(system__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def idc_id_filter(queryset, value):
        return queryset.filter(idc_id__icontains=value)

    @staticmethod
    def rack_id_filter(queryset, value):
        return queryset.filter(rack_id__icontains=value)

    @staticmethod
    def disk_filter(queryset, value):
        return queryset.filter(disk__icontains=value)

    @staticmethod
    def memory_filter(queryset, value):
        return queryset.filter(memory__icontains=value)

    @staticmethod
    def use_filter(queryset, value):
        return queryset.filter(use__icontains=value)

    @staticmethod
    def project_filter(queryset, value):
        return queryset.filter(project__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)

class hostServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")
    host_id=django_filters.CharFilter(method="host_id_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    listen_port=django_filters.CharFilter(method="listen_port_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = hostServiceInfo
        fields = ['name', 'host_id','unit_name', 'dept_name', 'listen_port','status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def host_id_filter(queryset, value):
        return queryset.filter(host_id__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def listen_port_filter(queryset, value):
        return queryset.filter(listen_port__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)


class databaseFilter(django_filters.FilterSet):
    host_id=django_filters.CharFilter(method="host_id_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    db_name=django_filters.CharFilter(method="db_name_filter")
    db_version=django_filters.CharFilter(method="db_version_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = databaseInfo
        fields = ['host_id','unit_name', 'dept_name', 'db_name', 'db_version','status']

    @staticmethod
    def host_id_filter(queryset, value):
        return queryset.filter(host_id__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def db_name_filter(queryset, value):
        return queryset.filter(db_name__icontains=value)

    @staticmethod
    def db_versiond_filter(queryset, value):
        return queryset.filter(db_version__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)


class databaseDBFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")
    db_id=django_filters.CharFilter(method="db_id_filter")
    unit_name=django_filters.CharFilter(method="unit_name_filter")
    dept_name=django_filters.CharFilter(method="dept_name_filter")
    use=django_filters.CharFilter(method="use_filter")
    status=django_filters.CharFilter(method="status_filter")

    class Meta:
        model = databaseDBInfo
        fields = ['name', 'db_id','unit_name', 'dept_name', 'use','status']

    @staticmethod
    def name_filter(queryset, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def db_id_filter(queryset, value):
        return queryset.filter(db_id__icontains=value)

    @staticmethod
    def unit_name_filter(queryset, value):
        return queryset.filter(unit_name__icontains=value)

    @staticmethod
    def dept_name_filter(queryset, value):
        return queryset.filter(dept_name__icontains=value)

    @staticmethod
    def use_filter(queryset, value):
        return queryset.filter(use__icontains=value)

    @staticmethod
    def status_filter(queryset, value):
        return queryset.filter(status=value)
