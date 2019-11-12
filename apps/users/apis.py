#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 21:11
# @file : apis.py
# @software : PyCharm

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import UserSerializers

######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.sessions.models import Session

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage

@api_view()
def UserListView(request):
    # 页面选择
    web_chose_left_1 = 'user_management'
    web_chose_left_2 = 'user_list'
    web_chose_middle = ''

    # 用户
    users = UserProfile.objects.all()
    units = UserCompany.objects.all()
    depts = UserDepartment.objects.all()

    # 用户选择
    user_check = request.GET.get('user_check', 'all')

    # 正常
    if user_check == 'up':
        users = users.filter(status=1)

    # 停用
    if user_check == 'down':
        users = users.filter(status=2)

    # 男性
    if user_check == '1':
        users = users.filter(gender='2')

    # 女性
    if user_check == '1':
        users = users.filter(gender='2')

    # 查询
    keyword = request.GET.get('keyword', '')

    if keyword != '':
        users = users.filter(
            Q(username__icontains=keyword) | Q(email__icontains=keyword) | Q(user_name__icontains=keyword)
            | Q(mobile__icontains=keyword))

    # 判断页码
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    # 对取到的数据进行分页，记得定义每页的数量
    p = Paginator(users, 12, request=request)

    # 分页处理后的 QuerySet
    users = p.page(page)

    context = {
        'web_chose_left_1': web_chose_left_1,
        'web_chose_left_2': web_chose_left_2,
        'web_chose_middle': web_chose_middle,
        'users': users,
        'units': units,
        'depts': depts,
        'user_check': user_check,
        'keyword': keyword,
    }
    return render(request, 'users/units/user_list.html', context=context)