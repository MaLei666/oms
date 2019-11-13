#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-11-12 21:11
# @file : user.py
# @software : PyCharm

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from users.models import *
from users.serializers import UserSerializer,UserInfoSerializer

######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from rest_framework.request import Request

#Todo
@csrf_exempt
def UserlistView(request):
    serializer_context = {
        'request': Request(request),
    }
    if request.method == 'GET':
        user = UserProfile.objects.all()
        serializer = UserSerializer(user, many=True,context =serializer_context)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data,context =serializer_context)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201,context = {'request': request})
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request,user_id):
    serializer_context = {
        'request': Request(request),
    }
    try:
        user = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserInfoSerializer(user,context =serializer_context)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data,context =serializer_context)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)



    # 页面选择
    # web_chose_left_1 = 'user_management'
    # web_chose_left_2 = 'user_list'
    # web_chose_middle = ''
    #
    # # 用户
    # users = UserProfile.objects.all()
    # units = UserCompany.objects.all()
    # depts = UserDepartment.objects.all()
    #
    # # 用户选择
    # user_check = request.GET.get('user_check', 'all')
    #
    # # 正常
    # if user_check == 'up':
    #     users = users.filter(status=1)
    #
    # # 停用
    # if user_check == 'down':
    #     users = users.filter(status=2)
    #
    # # 男性
    # if user_check == '1':
    #     users = users.filter(gender='2')
    #
    # # 女性
    # if user_check == '2':
    #     users = users.filter(gender='2')
    #
    # # 查询
    # keyword = request.GET.get('keyword', '')
    #
    # if keyword != '':
    #     users = users.filter(
    #         Q(username__icontains=keyword) | Q(email__icontains=keyword) | Q(user_name__icontains=keyword)
    #         | Q(mobile__icontains=keyword))
    #
    # # 判断页码
    # try:
    #     page = request.GET.get('page', 1)
    # except PageNotAnInteger:
    #     page = 1
    #
    # # 对取到的数据进行分页，记得定义每页的数量
    # p = Paginator(users, 12, request=request)
    #
    # # 分页处理后的 QuerySet
    # users = p.page(page)
    #
    # context = {
    #     'web_chose_left_1': web_chose_left_1,
    #     'web_chose_left_2': web_chose_left_2,
    #     'web_chose_middle': web_chose_middle,
    #     'users': users,
    #     'units': units,
    #     'depts': depts,
    #     'user_check': user_check,
    #     'keyword': keyword,
    # }
    # return render(request, 'users/units/user_list.html', context=context)