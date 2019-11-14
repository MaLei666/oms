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
from django.http import HttpResponse,JsonResponse,Http404
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
from rest_framework.views import APIView
from rest_framework import status,generics

# Todo
# @csrf_exempt
class UserlistApi(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # def get(self,request,format=None):
    #     user = UserProfile.objects.all()
    #     serializer = UserSerializer(user, many=True, context={'request': Request(request)})
    #     return JsonResponse(serializer.data)
    #
    # def post(self,request,format=None):
    #     data = JSONParser().parse(request)
    #     serializer = UserSerializer(data=data,context ={'request': Request(request)})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
class UserInfoApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'

    # def get_object(self,user_id):
    #     try:
    #         return UserProfile.objects.get(id=user_id)
    #     except UserProfile.DoesNotExist:
    #         return Http404
    #
    # def get(self, request, user_id, format=None):
    #     user = self.get_object(user_id)
    #     serializer = UserInfoSerializer(user,context ={'request': Request(request)})
    #     return JsonResponse(serializer.data)
    #
    # def put(self, request, user_id, format=None):
    #     user = self.get_object(user_id)
    #     serializer = UserInfoSerializer(user, data=user.data,context ={'request': Request(request)})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, user_id, format=None):
    #     user = self.get_object(user_id)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

