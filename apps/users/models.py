######################################
# Django 模块
######################################
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


######################################
# 系统模块
######################################
import datetime


__all__=['UserProfile','UserDepartment','UserCompany','UserLoginInfo','UserEmailVirificationCode','ROLE_CHOICES',
         'STATUS_CHOICES','GENDER_CHOICES','EMAIL_CHOICES','ACTION_CHOICES']

ROLE_CHOICES=((0, '后台开发者'),(1, '超级管理员'), (2, '平台管理员'), (3, '单位管理员'),(4, '部门管理员'),(5,'一般用户'))
STATUS_CHOICES=((1, '正常'), (0, '停用'))
GENDER_CHOICES=((1, '男'), (2, '女'))
EMAIL_CHOICES=(('register', '注册'), ('forget', '忘记密码'), ('change_email', '修改邮箱绑定'), ('active', '用户激活'))
ACTION_CHOICES=((1, '登录'), (2, '注销'))

######################################
# 单位表
######################################
class UserCompany(models.Model):
    name = models.CharField(verbose_name='单位名称', max_length=30,unique=True,)
    connect = models.CharField(verbose_name='联系人', max_length=30, blank=True, null=True)
    connect_phone=models.CharField(verbose_name='联系电话',max_length=30, blank=True, null=True)
    address = models.CharField(verbose_name='地址', max_length=50, blank=True, null=True)
    create_user=models.CharField(verbose_name='创建者',max_length=45,null=True,blank=True)
    user_id_create=models.BigIntegerField(verbose_name='创建用户id',null=True,blank=True)
    create_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True,null=True,blank=True)
    update_user=models.CharField(verbose_name='更新者',max_length=45,blank=True,null=True)
    update_time=models.DateTimeField(verbose_name='更新时间',blank=True,null=True)
    comment=models.CharField(verbose_name='备注',blank=True,null=True,max_length=1000)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)


    class Meta:
        verbose_name = '单位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 部门表
######################################
class UserDepartment(models.Model):
    name = models.CharField(verbose_name='部门名称', max_length=20)
    unit = models.ForeignKey(UserCompany, verbose_name='所属单位ID', on_delete=models.CASCADE)
    unit_name=models.CharField(verbose_name='所属单位',max_length=30)
    connect = models.CharField(verbose_name='联系人', max_length=30, blank=True, null=True)
    connect_phone = models.CharField(verbose_name='联系电话', max_length=30, blank=True, null=True)
    create_user = models.CharField(verbose_name='创建者', max_length=45,null=True,blank=True)
    user_id_create=models.BigIntegerField(verbose_name='创建用户id',null=True,blank=True)
    create_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True,null=True,blank=True)
    update_user = models.CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = models.DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment = models.CharField(verbose_name='备注', blank=True, null=True, max_length=1000)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)


    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name
        unique_together=('unit','name')

    def __str__(self):
        return self.name

#
# ######################################
# # 职位表
# ######################################
# class UserPosition(models.Model):
#     name = models.CharField(verbose_name='职位', max_length=20)
#     department = models.ForeignKey(UserDepartment, verbose_name='部门', on_delete=models.CASCADE)
#     desc = models.CharField(verbose_name='描述', max_length=200, blank=True, null=True)
#     add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
#
#     class Meta:
#         verbose_name = '职位'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return "%s - %s - %s" % (self.department.company.name, self.department.name, self.name)


######################################
# 用户扩展表
######################################
class UserProfile(AbstractUser):
    role = models.PositiveSmallIntegerField(verbose_name='角色', choices=ROLE_CHOICES,null=True,blank=True)
    user_name = models.CharField(verbose_name='用户姓名', max_length=10)
    unit_id=models.IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name=models.CharField(verbose_name='单位名称',max_length=100, null=True, blank=True)
    dept_id=models.IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name=models.CharField(verbose_name='部门名称',max_length=100, null=True, blank=True)
    mobile = models.CharField(verbose_name='手机号', max_length=20, null=True, blank=True)
    # avatar = models.CharField(verbose_name='用户头像', max_length=200, upload_to='users/avatar/%Y/%m',
    #                            default='users/avatar/default.png', null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_CHOICES, default='1',null=True, blank=True)
    # position = models.ForeignKey(UserPosition, verbose_name='职位', on´_delete=models.CASCADE, blank=True, null=True)
    user_id_create=models.BigIntegerField(verbose_name='创建用户id',null=True,blank=True)
    create_user = models.CharField(verbose_name='创建者', max_length=45,null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = models.CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = models.DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment = models.CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    # 获取账户添加时间
    def get_join_days(self):
        join_days = ((datetime.datetime.now() - self.date_joined).days + 1)
        return join_days

######################################
# 邮箱验证码表
######################################
class UserEmailVirificationCode(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=20)
    email = models.EmailField(verbose_name='接收邮箱')
    purpose = models.CharField(verbose_name='用途', choices=EMAIL_CHOICES, max_length=20)
    is_use = models.BooleanField(verbose_name='是否被使用', default=False)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

######################################
# 用户登录信息表
######################################
class UserLoginInfo(models.Model):
    action = models.PositiveSmallIntegerField(verbose_name='动作', choices=ACTION_CHOICES, default=1)
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    agent = models.CharField(verbose_name='客户端', max_length=200)
    ip = models.GenericIPAddressField(verbose_name='IP地址')
    address = models.CharField(verbose_name='登录地区', max_length=100)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户登录信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


######################################
# 用户反馈
######################################
# class UserAskHelp(models.Model):
#     user = models.ForeignKey(UserProfile, verbose_name='发送者', related_name='ah_user', on_delete=models.CASCADE)
#     subject = models.CharField(verbose_name='标题', max_length=100)
#     content = models.TextField(verbose_name='正文')
#     add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
#
#     class Meta:
#         verbose_name = '用户反馈'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.user.username

