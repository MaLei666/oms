#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 19:25
# @file : adminx.py
# @software : PyCharm

######################################
# Django 模块
######################################
import xadmin
from xadmin.layout import Row,Fieldset
from xadmin import views
######################################
# 自己写的模块
######################################


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = u"运维管理平台"
    site_footer = u"power by ml"
    menu_style = "accordion"

    # def get_site_menu(self):
    #     return [
    #         {
    #             'title': '自定义菜单',
    #             'icon': 'fa fa-bars',       # Font Awesome图标
    #             'menus':(
    #                 {
    #                     'title': '平台用户',
    #                     'icon': 'fa fa-bug',
    #                     'url': self.get_model_url(userProfile,'changelist')
    #
    #                 },
    #
    #             )
    #         },
            # {
            #     'title': 'Bug统计',
            #     'icon': 'fa fa-bug',
            #     'menus':(
            #         {
            #             'title': 'Bug表',
            #             'icon': 'fa fa-bug',
            #             'url': "https://www.cnblogs.com/yoyoketang/"  # 自定义跳转列表
            #
            #         },)
            # }

        # ]
######################################
# 注册
######################################

xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)
