#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-12-03 15:26
# @file : code_response.py
# @software : PyCharm

import time
class response_fomat:
    res_json={
        "code": "",
        "message":"",
        "timestamp":int(round(time.time() * 1000))}

    def __init__(self):
        self.res_json=response_fomat.res_json

    def request_add_succeed(self):
        self.res_json['code']=1000
        self.res_json['message'] = '添加成功！'
        return self.res_json

    def request_edit_succeed(self):
        self.res_json['code']=1000
        self.res_json['message'] = '修改成功！'
        return self.res_json

    def request_delete_succeed(self):
        self.res_json['code']=1000
        self.res_json['message'] = '删除成功！'
        return self.res_json

    def no_permission(self):
        self.res_json['code']=1001
        self.res_json['message'] = '当前用户无权限！'
        return self.res_json

    def duplicate_data(self):
        self.res_json['code'] = 1002
        self.res_json['message'] = '数据已存在！'
        return self.res_json

    def status_outage(self):
        self.res_json['code']=1003
        self.res_json['message'] = '当前用户已被禁用，请联系管理员！'
        return self.res_json

    def status_abnormal(self):
        self.res_json['code']=1004
        self.res_json['message'] = '当前用户状态异常，请联系管理员！'
        return self.res_json

    def loginout_success(self):
        self.res_json['code'] = 1005
        self.res_json['message'] = '退出成功！'
        return self.res_json

    def password_discord (self):
        self.res_json['code'] = 1006
        self.res_json['message'] = '两次密码不一致！'
        return self.res_json

    def password_wrong(self):
        self.res_json['code'] = 1007
        self.res_json['message'] = '密码输入错误！'
        return self.res_json

    def data_illegal(self):
        self.res_json['code'] = 1007
        self.res_json['message'] = '数据不合法！'
        return self.res_json

    def authenticat_failed(self):
        self.res_json['code'] = 1008
        self.res_json['message'] = '用户认证失败！'
        return self.res_json

    def http_error(self):
        self.res_json['code']=201
        self.res_json['message'] = 'request http error'
        return self.res_json

    def params_error(self):
        self.res_json['code']=202
        self.res_json['message'] = 'request params error'
        return self.res_json

    def signature_error(self):
        self.res_json['code']=203
        self.res_json['message'] = 'request signature error'
        return self.res_json

    def data_handle_succeed(self):
        self.res_json['code']=1000
        self.res_json['message'] = 'data handle succeeded'
        return self.res_json

    def data_handle_failed(self):
        self.res_json['code']=1001
        self.res_json['message'] = 'data handle failed'
        return self.res_json

    def data_not_found(self):
        self.res_json['code']=1003
        self.res_json['message'] = 'data not found'
        return self.res_json

    def data_handle_unusual(self):
        self.res_json['code']=1004
        self.res_json['message'] = 'data handle unusual'
        return self.res_json

    def internal_server_error(self):
        self.res_json['code']=1005
        self.res_json['message'] = '系统错误，请联系管理员！'
        return self.res_json

    def device_offline_error(self):
        self.res_json['code']=1006
        self.res_json['message'] = 'Reset request offline'
        return self.res_json

