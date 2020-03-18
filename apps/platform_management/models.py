######################################
# Django 模块
######################################
from django.db.models import Model,CharField,DateTimeField,ForeignKey,PositiveSmallIntegerField,BigIntegerField,IntegerField

######################################
# 自定义模块
######################################
from users.models import userProfile

__all__=['platformInfo','platformUserInfo']


STATUS_CHOICES=((1, '正常'), (0, '停用'))
BELONG_CHOICES=((1, '公司公用平台'), (2, '部门内部平台'),(3, '第三方公用平台'))
######################################
# 平台表
######################################
class platformInfo(Model):
    name = CharField(verbose_name='平台名称', max_length=200)
    url = CharField(verbose_name='url', max_length=200)
    belong = PositiveSmallIntegerField(verbose_name='隶属', choices=BELONG_CHOICES)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = '平台'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 平台用户表
######################################
class platformUserInfo(Model):
    platform_id = IntegerField(verbose_name='平台id')
    platform=CharField(verbose_name='平台名称', max_length=200)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    username = CharField(verbose_name='用户名称', max_length=30, blank=True, null=True)
    password = CharField(verbose_name='密码', max_length=50, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = '平台用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.platform, self.username)





