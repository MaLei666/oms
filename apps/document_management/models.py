######################################
# Django 模块
######################################
from django.db.models import Model,CharField,DateTimeField,ForeignKey,TextField,IntegerField,BigIntegerField

######################################
# 系统模块
######################################
import datetime

######################################
# 自定义模块
######################################
from users.models import userProfile

__all__=['Document']

BELONG_CHOICE=((1, '文档'), (2, 'Shell脚本'), (3, 'Python脚本'), (4, '其他'))
STATUS_CHOICE=((1, '正常'), (0, '停用'))
######################################
# 文档表
######################################
class Document(Model):
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    subject = CharField(verbose_name='标题', max_length=200)
    tags_id=IntegerField(verbose_name='标签ID', null=True, blank=True)
    tags = CharField(verbose_name='分类标签',max_length=200, null=True, blank=True)
    content = TextField(verbose_name='内容', null=True, blank=True)
    belong = IntegerField(verbose_name='隶属', choices=BELONG_CHOICE,default=4)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = IntegerField(verbose_name='状态', choices=STATUS_CHOICE,default=1)

    class Meta:
        verbose_name = '文档'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject



























