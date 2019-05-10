"""
User app
"""
from django.urls import path
from .views import *


app_name = 'spider_data'

urlpatterns = [
    # 问题列表页
    path('questionlist', Zhihu_Q_View.as_view(), name='zhihu_list'),
    path('answerlist/<int:question_id>', Zhihu_A_View.as_view(), name='zhihu_info'),
    path('dplist', DP_T_View.as_view(), name='dp_list'),
    path('sinfo/<int:tip_id>', DP_S_View.as_view(), name='dp_info'),
    path('rwinfo/<str:shopId>', DP_RE_View.as_view(), name='dp_rw_info'),

]


