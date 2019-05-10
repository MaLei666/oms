from django.shortcuts import render
from utils.login_check import LoginStatusCheck
from django.views import View
from django.http import HttpResponse

from .forms import *
from .models import *
from django.db.models import Q
######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
######################################
# 产品列表
######################################
class Artifact_List_View(LoginStatusCheck, View):
    def get(self, request):
        if request.user.role > 1:
            # 页面选择
            web_chose_left_1 = 'vechain'
            web_chose_left_2 = 'artifact'
            web_chose_middle = ''

            # 产品
            artifact_records=ArtifactInfo.objects.filter(status=1)

            # 关键字
            keyword = request.GET.get('keyword', '')
            if keyword != '':
                artifact_records = artifact_records.filter(Q(artifact__icontains=keyword))

            # 记录数量
            record_nums = artifact_records.count()

            # 判断页码
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            # 对取到的数据进行分页，记得定义每页的数量
            p = Paginator(artifact_records, 16, request=request)

            # 分页处理后的 QuerySet
            artifact_records = p.page(page)

            context = {
                'web_chose_left_1': web_chose_left_1,
                'web_chose_left_2': web_chose_left_2,
                'web_chose_middle': web_chose_middle,
                'artifact_records': artifact_records,
                'record_nums': record_nums
            }
            return render(request, 'vechain/artifact_list.html', context=context)
        else:
            return HttpResponse(status=403)

