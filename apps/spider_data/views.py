######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse

######################################
# 系统模块
######################################
import json
import datetime
from .forms import *
from .models import *
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage


######################################
# 问题列表
######################################
class Zhihu_Q_View(View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'spider_data'
        web_chose_left_2 = 'zhihu_list'
        web_chose_middle = ''

        # 获取问题记录
        question_records = ZhihuList.objects.order_by('id')

        # 关键字
        # keyword = request.GET.get('keyword', '')

        # if keyword != '':
        #     host_records = question_records.filter(Q(hot__icontains=keyword) | Q(
        #         use__name__icontains=keyword) | Q(project__name__icontains=keyword) | Q(desc__icontains=keyword))

        # 记录数量
        record_nums = question_records.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(question_records, 10, request=request)

        # 分页处理后的 QuerySet
        question_records = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'question_records': question_records,
            'record_nums': record_nums,
        }
        return render(request, 'spider_data/zhihu_list.html', context=context)


######################################
# 问题回答列表
######################################
class  Zhihu_A_View(View):
    def get(self, request,question_id):
        # 页面选择
        web_chose_left_1 = 'spider_data'
        web_chose_left_2 = 'zhihu_question'
        web_chose_middle = ''

        # 获取问题详情
        answer_records = ZhihuInfo.objects.order_by('-voteup_count').filter(question_id=question_id)

        # 关键字
        # keyword = request.GET.get('keyword', '')

        # if keyword != '':
        #     host_records = data_records.filter(Q(hot__icontains=keyword) | Q(
        #         use__name__icontains=keyword) | Q(project__name__icontains=keyword) | Q(desc__icontains=keyword))

        # 记录数量
        record_nums = answer_records.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(answer_records,10, request=request)

        # 分页处理后的 QuerySet
        answer_records = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'answer_records': answer_records,
            'record_nums': record_nums,
        }
        return render(request, 'spider_data/zhihu_info.html', context=context)


######################################
# 大众点评分类列表
######################################
class DP_T_View(View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'spider_data'
        web_chose_left_2 = 'dp_list'
        web_chose_middle = ''

        # 获取分类列表
        tip_records = FoodRank.objects.values('tip','tip_id').distinct()

        # 关键字
        # keyword = request.GET.get('keyword', '')

        # if keyword != '':
        #     host_records = data_records.filter(Q(hot__icontains=keyword) | Q(
        #         use__name__icontains=keyword) | Q(project__name__icontains=keyword) | Q(desc__icontains=keyword))

        # 记录数量
        record_nums = tip_records.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(tip_records, 10, request=request)

        # 分页处理后的 QuerySet
        tip_records = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'tip_records': tip_records,
            'record_nums': record_nums,
        }
        return render(request, 'spider_data/dp_list.html', context=context)


######################################
# 大众点评店铺列表
######################################
class DP_S_View(View):
    def get(self, request,tip_id):
        # 页面选择
        web_chose_left_1 = 'spider_data'
        web_chose_left_2 = 'dp_shop_info'
        web_chose_middle = ''

        # 获取店铺信息
        shop_infos = FoodRank.objects.filter(tip_id=tip_id)

        # 关键字
        # keyword = request.GET.get('keyword', '')

        # if keyword != '':
        #     host_records = data_records.filter(Q(hot__icontains=keyword) | Q(
        #         use__name__icontains=keyword) | Q(project__name__icontains=keyword) | Q(desc__icontains=keyword))

        # 记录数量
        record_nums = shop_infos.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(shop_infos, 10, request=request)

        # 分页处理后的 QuerySet
        shop_infos = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'shop_infos': shop_infos,
            'record_nums': record_nums,
        }
        return render(request, 'spider_data/dp_shop_info.html', context=context)

######################################
# 大众点评店铺评论列表
######################################
class DP_RE_View(View):
    def get(self, request,shopId):
        # 页面选择
        web_chose_left_1 = 'spider_data'
        web_chose_left_2 = 'dp_re_info'
        web_chose_middle = ''

        # 获取评论信息
        re_infos = ShopInfo.objects.filter(shopId=shopId)

        # 关键字
        # keyword = request.GET.get('keyword', '')

        # if keyword != '':
        #     host_records = data_records.filter(Q(hot__icontains=keyword) | Q(
        #         use__name__icontains=keyword) | Q(project__name__icontains=keyword) | Q(desc__icontains=keyword))

        # 记录数量
        record_nums = re_infos.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(re_infos, 20, request=request)

        # 分页处理后的 QuerySet
        re_infos = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            're_infos': re_infos,
            'record_nums': record_nums,
        }
        return render(request, 'spider_data/dp_re_info.html', context=context)





