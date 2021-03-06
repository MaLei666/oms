######################################
# Django 模块
######################################
from django import forms


######################################
# 自定义模块
######################################
# from .forms import *


######################################
# 用户登录表单
######################################
class UerLoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4, required=True)
    password = forms.CharField(max_length=20, min_length=6, required=True)


######################################
# 用户忘记密码表单
######################################
class UserForgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)


######################################
# 修改用户信息表单
######################################
class ChangeUserInfoForm(forms.Form):
    user_name = forms.CharField(max_length=10)
    mobile = forms.CharField(max_length=20, required=False)
    gender = forms.IntegerField()
    # position = forms.ForeignKey(UserPosition, verbose_name='职位', on´_delete=forms.CASCADE, required=False)
    comment = forms.CharField(max_length=200, required=False)


######################################
# 修改用户密码表单
######################################
class ChangeUserPasswordForm(forms.Form):
    cur_password = forms.CharField(min_length=6, max_length=20, required=True)
    new_password = forms.CharField(min_length=6, max_length=20, required=True)
    renew_password = forms.CharField(min_length=6, max_length=20, required=True)

######################################
# 添加单位表单
######################################
class AddUnitForm(forms.Form):
    name = forms.CharField(max_length=30,required=True)
    connect = forms.CharField(max_length=30,required=False)
    connect_phone = forms.CharField(max_length=30,required=False)
    comment = forms.CharField( max_length=200,required=False)
    address = forms.CharField( max_length=50,required=False)

######################################
# 修改单位表单
######################################
class EditUnitForm(forms.Form):
    name = forms.CharField(max_length=30,required=True)
    connect = forms.CharField(max_length=30,required=False)
    connect_phone = forms.CharField(max_length=30,required=False)
    comment = forms.CharField( max_length=200,required=False)
    address = forms.CharField( max_length=50,required=False)

######################################
# 添加部门表单
######################################
class AddDeptForm(forms.Form):
    name = forms.CharField(max_length=20,required=True)
    connect = forms.CharField(max_length=30,required=False)
    connect_phone = forms.CharField( max_length=30,required=False)
    comment = forms.CharField(max_length=1000,required=False)

######################################
# 修改部门表单
######################################
class EditDeptForm(forms.Form):
    name = forms.CharField(max_length=20,required=True)
    connect = forms.CharField(max_length=30,required=False)
    connect_phone = forms.CharField( max_length=30,required=False)
    comment = forms.CharField( max_length=1000,required=False)

######################################
# 添加用户表单
######################################
class AddUserForm(forms.Form):
    user_name = forms.CharField(max_length=20, required=True)
    # mobile = forms.CharField(min_length=6, max_length=20, required=True)
    # password = forms.CharField(min_length=6, max_length=20, required=True)


######################################
# 修改用户表单
######################################
class EditUserForm(forms.Form):
    user_name = forms.CharField(max_length=20, required=True)









