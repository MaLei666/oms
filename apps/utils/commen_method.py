#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020-02-20 15:32
# @file : commen_method.py
# @software : PyCharm
__all__=['UserOperation','login_info']

from operation_record.models import UserOperationRecord
from users.models import UserLoginInfo

def UserOperation(op_user,username,user_name,role,unit_id,unit_name,dept_id,dept_name
                  ,belong,status,op_num,operation,action):
    try:
        op_record = UserOperationRecord()
        op_record.op_user = op_user
        op_record.username = username
        op_record.user_name = user_name
        op_record.role = role
        op_record.unit_id = unit_id
        op_record.unit_name = unit_name
        op_record.dept_id = dept_id
        op_record.dept_name = dept_name
        op_record.belong = belong
        op_record.status = status
        op_record.op_num = op_num
        op_record.operation = operation
        op_record.action = action
        op_record.save()
        return 0
    except Exception as e:
        return e

def login_info(action,user,username,user_name,role,unit_id,unit_name,dept_id,dept_name,agent,ip,address):
    login_record = UserLoginInfo()
    login_record.action = action
    login_record.user = user
    login_record.username=username
    login_record.user_name=user_name
    login_record.role=role
    login_record.unit_id=unit_id
    login_record.unit_name=unit_name
    login_record.dept_id=dept_id
    login_record.dept_name=dept_name
    login_record.agent = agent
    login_record.ip = ip
    login_record.address = address
    login_record.save()
    return 0