######################################
# Django 模块
######################################
from django import forms


######################################
# 自定义模块
######################################
from .models import *


######################################
# 添加主机表单
######################################
class AddHostInfoForm(forms.Form):
    in_ip = forms.GenericIPAddressField(required=True)
    hostname = forms.CharField(min_length=2, max_length=20, required=True)
    # cpu = forms.CharField(min_length=5, max_length=50, required=True)
    # disk = forms.IntegerField(required=True)
    # memory = forms.IntegerField(required=True)
    # network = forms.IntegerField(required=True)
    ssh_port = forms.IntegerField(required=True)
    admin_user = forms.CharField(min_length=2, max_length=20, required=True)
    admin_pass = forms.CharField(min_length=6, max_length=50, required=True)
    # normal_user = forms.CharField(min_length=2, max_length=20, required=False)
    # normal_pass = forms.CharField(min_length=2, max_length=50, required=False)


######################################
# 修改主机表单
######################################
class EditHostInfoForm(forms.Form):
    in_ip = forms.GenericIPAddressField(required=True)
    hostname = forms.CharField(min_length=2, max_length=20, required=True)
    # cpu = forms.CharField(min_length=5, max_length=50, required=True)
    # disk = forms.IntegerField(required=True)
    # memory = forms.IntegerField(required=True)
    # network = forms.IntegerField(required=True)
    ssh_port = forms.IntegerField(required=True)
    admin_user = forms.CharField(min_length=2, max_length=20, required=True)
    admin_pass = forms.CharField(min_length=6, max_length=50, required=True)
    # normal_user = forms.CharField(min_length=2, max_length=20, required=False)
    # normal_pass = forms.CharField(min_length=2, max_length=50, required=False)


######################################
# 添加服务表单
######################################
class AddHostServiceForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    version = forms.CharField(max_length=20, required=True)
    listen_user = forms.CharField(max_length=20, required=True)
    listen_port = forms.CharField(max_length=30, required=True)
    ins_path = forms.CharField(max_length=100, required=True)
    log_path = forms.CharField(max_length=100, required=True)
    backup_path = forms.CharField(max_length=100, required=False)
    start_cmd = forms.CharField(max_length=100, required=True)
    desc = forms.CharField(max_length=200, required=False)


######################################
# 编辑服务表单
######################################
class EditHostServiceForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    version = forms.CharField(max_length=20, required=True)
    listen_user = forms.CharField(max_length=20, required=True)
    listen_port = forms.CharField(max_length=30, required=True)
    ins_path = forms.CharField(max_length=100, required=True)
    log_path = forms.CharField(max_length=100, required=True)
    backup_path = forms.CharField(max_length=100, required=False)
    start_cmd = forms.CharField(max_length=100, required=True)
    desc = forms.CharField(max_length=200, required=False)

######################################
# 添加系统表单
######################################
class AddOsForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    version = forms.CharField(max_length=20, required=True)

######################################
# 添加项目
######################################
class AddProjectForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    run_env = forms.CharField(max_length=20, required=True)


######################################
# 编辑项目
######################################
class EditProjectForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    run_env = forms.CharField(max_length=20, required=True)

######################################
# 添加用途
######################################
class AddUseForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)

######################################
# 编辑用途
######################################
class EditUseForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
######################################
# 编辑系统表单
######################################
class EditOsForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    version = forms.CharField(max_length=20, required=True)

######################################
# 添加数据库信息
######################################
class AddDatabaseInfoForm(forms.Form):
    db_name = forms.CharField(min_length=2, max_length=20, required=True)
    db_version = forms.CharField(max_length=20, required=True)
    db_admin_user = forms.CharField(min_length=2, max_length=20, required=True)
    db_admin_pass = forms.CharField(min_length=2, max_length=50, required=True)

######################################
# 修改数据库信息
######################################
class EditDatabaseInfoForm(forms.Form):
    db_name = forms.CharField(min_length=2, max_length=20, required=True)
    db_version = forms.CharField(max_length=20, required=True)
    db_admin_user = forms.CharField(min_length=2, max_length=20, required=True)
    db_admin_pass = forms.CharField(min_length=2, max_length=50, required=True)


######################################
# 添加数据库库表
######################################
class AddDatabaseDBForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    status=forms.IntegerField(required=True)



######################################
# 编辑数据库库表
######################################
class EditDatabaseDBForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)

######################################
# 添加数据库用户
######################################
class AddDatabaseUserForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=20, required=True)
    password = forms.CharField(min_length=2, max_length=50, required=True)
    grant_login = forms.CharField(max_length=50, required=True)


######################################
# 编辑数据库用户
######################################
class EditDatabaseUserForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=20, required=True)
    password = forms.CharField(min_length=2, max_length=50, required=True)
    grant_login = forms.CharField(max_length=50, required=True)

######################################
# 添加映射
######################################
class AddPortToPortForm(forms.Form):
    ip_out = forms.GenericIPAddressField(required=False)
    port_out = forms.IntegerField(required=True)
    ip_in = forms.GenericIPAddressField(required=True)
    port_in = forms.IntegerField(required=True)
    use = forms.CharField(max_length=20, required=False)
    desc = forms.CharField(max_length=200, required=False)


######################################
# 编辑映射
######################################
class EditPortToPortForm(forms.Form):
    ip_out = forms.GenericIPAddressField(required=False)
    port_out = forms.IntegerField(required=True)
    ip_in = forms.GenericIPAddressField(required=True)
    port_in = forms.IntegerField(required=True)
    use = forms.CharField(max_length=20, required=False)
    desc = forms.CharField(max_length=200, required=False)


######################################
# 添加域名
######################################
class AddDomainNameForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)


######################################
# 修改域名
######################################
class EditDomainNameForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)


######################################
# 添加域名解析
######################################
class AddDomainNameResolveForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    ip = forms.GenericIPAddressField(required=True)


######################################
# 修改域名解析
######################################
class EditDomainNameResolveForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    ip = forms.GenericIPAddressField(required=True)

######################################
# 添加数据字典
######################################
class AddDictForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    value=forms.CharField(max_length=200,required=True)


######################################
# 修改数据字典
######################################
class EditDictForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    value = forms.CharField(max_length=200, required=True)
