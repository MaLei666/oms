#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020-02-20 15:32
# @file : commen_method.py
# @software : PyCharm
__all__=['UserOperation','login_info']

from operation_record.models import UserOperationRecord
from users.models import UserLoginInfo

def UserOperation(op_user,belong,status,op_num,operation,action):
    try:
        op_record = UserOperationRecord()
        op_record.user = op_user.id
        op_record.username = op_user.username
        op_record.user_name = op_user.user_name
        op_record.role = op_user.role
        op_record.user_id=op_user.id
        op_record.unit_id = op_user.unit_id
        op_record.unit_name = op_user.unit_name
        op_record.dept_id = op_user.dept_id
        op_record.dept_name = op_user.dept_name
        op_record.belong = belong
        op_record.status = status
        op_record.op_num = op_num
        op_record.operation = operation
        op_record.action = action
        op_record.save()
        return 0
    except Exception as e:
        return e

def login_info(action,user,agent,ip):
    login_record = UserLoginInfo()
    login_record.action = action
    login_record.user = user.id
    login_record.username=user.username
    login_record.user_name=user.user_name
    login_record.role=user.role
    login_record.unit_id=user.unit_id
    login_record.unit_name=user.unit_name
    login_record.dept_id=user.dept_id
    login_record.dept_name=user.dept_name
    login_record.agent = agent
    login_record.ip = ip
    login_record.address = user.address
    login_record.save()
    return 0