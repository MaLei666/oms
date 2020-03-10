

__all__=['UserOperationRecord']

from django.db.models import Model,CharField,DateTimeField,IntegerField,ForeignKey,\
    PositiveSmallIntegerField,CASCADE
from users.models import userProfile

ACTION_CHOICES=((1, '主机管理'), (2, '系统管理'), (3, '用户管理'), (4, '文档管理'),(5, '巡检监督'),(6,'数据字典'))
OPERATION_CHOICES=((1, '添加'), (2, '修改'), (3, '启用'), (4, '停用'), (5, '登录'), (6, '退出'))
STATUS_CHOICES=((1, '公开'), (2, '不公开'))
######################################
# 用户操作表
######################################
class UserOperationRecord(Model):
    user = IntegerField(verbose_name='操作用户id', default=1000)
    username = CharField(verbose_name='用户名', max_length=200)
    user_name = CharField(verbose_name='用户姓名', max_length=100, null=True, blank=True)
    role = IntegerField(verbose_name='用户角色', default=10)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    belong = PositiveSmallIntegerField(verbose_name='归属', choices=ACTION_CHOICES)
    operation = PositiveSmallIntegerField(verbose_name='操作', choices=OPERATION_CHOICES)
    op_num = IntegerField(verbose_name='被操作项目ID')
    action = CharField(verbose_name='操作详情', max_length=100)
    status = PositiveSmallIntegerField(verbose_name='公开程度', choices=STATUS_CHOICES)
    add_time = DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户操作表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ("%s - %s") % (self.username, self.action)


