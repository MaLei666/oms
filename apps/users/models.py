######################################
# Django 模块
######################################
from django.db.models import Model,CharField,DateTimeField,IntegerField,ForeignKey,\
    PositiveSmallIntegerField,GenericIPAddressField,EmailField,BigIntegerField,CASCADE
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

__all__=['userProfile','UserDepartment','UserCompany','UserLoginInfo','UserLoginInfo']

ROLE_CHOICES=((0, '后台开发者'),(1, '超级管理员'), (2, '平台管理员'), (3, '单位管理员'),(4, '部门管理员'),(5,'一般用户'))
STATUS_CHOICES=((1, '正常'), (0, '停用'))
GENDER_CHOICES=((1, '男'), (2, '女'))
EMAIL_CHOICES=(('register', '注册'), ('forget', '忘记密码'), ('change_email', '修改邮箱绑定'), ('active', '用户激活'))
ACTION_CHOICES=((1, '登录'), (2, '注销'))

######################################
# 单位表
######################################
class UserCompany(Model):
    name = CharField(verbose_name='单位名称', max_length=30,unique=True,)
    connect = CharField(verbose_name='联系人', max_length=30, blank=True, null=True)
    connect_phone=CharField(verbose_name='联系电话',max_length=30, blank=True, null=True)
    address = CharField(verbose_name='地址', max_length=200, blank=True, null=True)
    create_user=CharField(verbose_name='创建者',max_length=45,null=True,blank=True)
    user_id_create=BigIntegerField(verbose_name='创建用户id',null=True,blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True,null=True,blank=True)
    update_user=CharField(verbose_name='更新者',max_length=45,blank=True,null=True)
    update_time=DateTimeField(verbose_name='更新时间',blank=True,null=True)
    comment=CharField(verbose_name='备注',blank=True,null=True,max_length=1000)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)


    class Meta:
        verbose_name = '单位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 部门表
######################################
class UserDepartment(Model):
    name = CharField(verbose_name='部门名称', max_length=20)
    unit = ForeignKey(UserCompany, verbose_name='所属单位ID', on_delete=CASCADE)
    unit_name=CharField(verbose_name='所属单位',max_length=30, blank=True, null=True)
    connect = CharField(verbose_name='联系人', max_length=30, blank=True, null=True)
    connect_phone = CharField(verbose_name='联系电话', max_length=30, blank=True, null=True)
    create_user = CharField(verbose_name='创建者', max_length=45,null=True,blank=True)
    user_id_create=BigIntegerField(verbose_name='创建用户id',null=True,blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True,null=True,blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment = CharField(verbose_name='备注', blank=True, null=True, max_length=1000)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)


    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name
        unique_together=('unit','name')

    def __str__(self):
        return self.name

# ######################################
# # 职位表
# ######################################
# class UserPosition(Model):
#     name = CharField(verbose_name='职位', max_length=20)
#     desc = CharField(verbose_name='描述', max_length=200, blank=True, null=True)
#     add_time = DateTimeField(verbose_name='添加时间', auto_now_add=True)
#
#     class Meta:
#         verbose_name = '职位'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return "%s - %s - %s" % (self.department.company.name, self.department.name, self.name)

class MyBaseUserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.role = 0
        user.save(using=self._db)
        return user


######################################
# 用户扩展表
######################################
class userProfile(AbstractBaseUser):
    objects=MyBaseUserManager()
    role = PositiveSmallIntegerField(verbose_name='角色', choices=ROLE_CHOICES,null=True,blank=True)
    username=CharField(verbose_name='登录账号',max_length=100,unique=True)
    user_name = CharField(verbose_name='用户姓名', max_length=100)
    unit_id=IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name=CharField(verbose_name='单位名称',max_length=100, null=True, blank=True)
    dept_id=IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name=CharField(verbose_name='部门名称',max_length=100, null=True, blank=True)
    mobile = CharField(verbose_name='手机号', max_length=20, null=True, blank=True)
    address=CharField(verbose_name='居住地',max_length=200,null=True,blank=True)
    email=EmailField(verbose_name='电子邮件',null=True,blank=True)
    gender = IntegerField(verbose_name='性别', choices=GENDER_CHOICES, default='1',null=True, blank=True)
    position = CharField(verbose_name='职位',max_length=100,null=True,blank=True)
    user_id_create=BigIntegerField(verbose_name='创建用户id',null=True,blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45,null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment = CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['email']

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

######################################
# 用户登录信息表
######################################
class UserLoginInfo(Model):
    action = PositiveSmallIntegerField(verbose_name='动作', choices=ACTION_CHOICES, default=1)
    user = ForeignKey(userProfile, verbose_name='用户', on_delete=CASCADE)
    username=CharField(verbose_name='用户名',max_length=200)
    user_name = CharField(verbose_name='用户姓名', max_length=100, null=True, blank=True)
    role=IntegerField(verbose_name='用户角色',default=10)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    agent = CharField(verbose_name='客户端', max_length=200, blank=True, null=True)
    ip = GenericIPAddressField(verbose_name='IP地址', blank=True, null=True)
    address = CharField(verbose_name='登录地区', max_length=200, blank=True, null=True)
    add_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = '用户登录信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

