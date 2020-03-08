######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse, Http404
from django.views import View
from django.http import HttpResponse, StreamingHttpResponse
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage

######################################
# 系统模块
######################################
import json
import datetime, time
import re

######################################
# 自建模块
######################################
from utils.login_check import LoginStatusCheck
from .forms import *
from .models import *
from operation_record.models import UserOperationRecord


########################################################################################################################
## CKEDITOR 上传图片
########################################################################################################################
@csrf_protect
def upload_image(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            # path 修改上传的路径
            path = "media/ckeditor/image/" + time.strftime("%Y%m%d%H%M%S", time.localtime())
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")
            # 直接遍历类文件类型就可以生成迭代器了
            for chunk in f:
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception as e:
            print(e)
        res = r"<script>window.parent.CKEDITOR.tools.callFunction(" + callback + ",'/" + file_name + "', '');</script>"
        return HttpResponse(res)
    else:
        raise Http404()

##################################
# 下载文档
######################################
class DocumentDownloadView(LoginStatusCheck, View):
    def get(self, request, doc_id):
        if request.user.role <3:
            doc_info = Document.objects.get(id=int(doc_id))
            time_now = time.strftime("%Y%m%H%M%S", time.localtime())
            filename = doc_info.subject + '_' + time_now

            # 判断文件类型
            if doc_info.belong == 2:
                filename = filename + '.sh'
            elif doc_info.belong == 3:
                filename = filename + '.py'
            elif doc_info.belong == 4:
                filename = filename + '.bat'
            else:
                filename = filename + '.txt'

            # 文件内容获取
            content = doc_info.content
            content_re = re.compile(r'<code .*?>(.*?)</code>', re.S | re.M)
            content = content_re.findall(content)[0]
            content = content.replace("\r\n", '\n')

            # 下载文件
            response = StreamingHttpResponse(content)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename=' + filename.encode('utf-8').decode("ISO-8859-1")
            return response
        else:
            return HttpResponse(status=403)