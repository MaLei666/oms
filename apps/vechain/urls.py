#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-03-14 21:10
# @file : urls.py
# @software : PyCharm

"""
Host management app
"""
from django.urls import path
from vechain.views import *


app_name = 'vechain'

urlpatterns = [
    # 产品列表
    path('list', Artifact_List_View.as_view(), name='artifact_list'),
    ]


