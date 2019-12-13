#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-12-03 15:26
# @file : code_response.py
# @software : PyCharm

import time
class responseFomat:
    res_json={
        "code": "",
        "message":"",
        "timestamp":int(round(time.time() * 1000))}

    def __init__(self):
        self.res_json=responseFomat.res_json

    def requestAddSucceed(self):
        self.res_json['code']=1000
        self.res_json['message'] = '添加成功！'
        return self.res_json

    def requestEditSucceed(self):
        self.res_json['code']=1000
        self.res_json['message'] = '修改成功！'
        return self.res_json

    def requestDeleteSucceed(self):
        self.res_json['code']=1000
        self.res_json['message'] = '删除成功！'
        return self.res_json

    def noPermission(self):
        self.res_json['code']=1001
        self.res_json['message'] = '当前用户无权限！'
        return self.res_json

    def duplicateData(self):
        self.res_json['code'] = 1002
        self.res_json['message'] = '数据已存在！'
        return self.res_json

    def requestHttpError(self):
        self.res_json['code']=201
        self.res_json['message'] = 'request http error'
        return self.res_json

    def requestParamsError(self):
        self.res_json['code']=202
        self.res_json['message'] = 'request params error'
        return self.res_json

    def requestSignatureError(self):
        self.res_json['code']=203
        self.res_json['message'] = 'request signature error'
        return self.res_json

    def dataHandleSucceeded(self):
        self.res_json['code']=1000
        self.res_json['message'] = 'data handle succeeded'
        return self.res_json

    def dataHandleFailed(self):
        self.res_json['code']=1001
        self.res_json['message'] = 'data handle failed'
        return self.res_json

    def dataNotFound(self):
        self.res_json['code']=1003
        self.res_json['message'] = 'data not found'
        return self.res_json

    def dataHandleUnusual(self):
        self.res_json['code']=1004
        self.res_json['message'] = 'data handle unusual'
        return self.res_json

    def internalServerError(self):
        self.res_json['code']=1005
        self.res_json['message'] = 'internal server error'
        return self.res_json

    def deviceofflineError(self):
        self.res_json['code']=1006
        self.res_json['message'] = 'Reset request offline'
        return self.res_json

