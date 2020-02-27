######################################
# Django 模块
######################################
from django.db.models import Model,CharField,DateTimeField,ForeignKey,PositiveSmallIntegerField,CASCADE

######################################
# 自定义模块
######################################
from users.models import userProfile


######################################
# 平台表
######################################
class PlatformInfo(Model):
    name = CharField(verbose_name='平台名称', max_length=30)
    url = CharField(verbose_name='url', max_length=200)
    belong = PositiveSmallIntegerField(verbose_name='隶属', choices=((1, '公司平台'), (2, '第三方平台')))
    # is_public = BooleanField(verbose_name='公开', default=True)
    # add_user = ForeignKey(userProfile, verbose_name='添加人', related_name='pl_user', on_delete=CASCADE, default=1)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=((1, '正常'), (0, '停用')), default=1)

    class Meta:
        verbose_name = '平台表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 平台用户表
######################################
class PlatformUserInfo(Model):
    platform = ForeignKey(PlatformInfo, verbose_name='平台', related_name='pu_plat', on_delete=CASCADE)
    username = CharField(verbose_name='平台名称', max_length=30, blank=True, null=True)
    password = CharField(verbose_name='平台密码', max_length=50, blank=True, null=True)
    user = ForeignKey(userProfile, verbose_name='用户', related_name='pu_user', on_delete=CASCADE)
    update_user = ForeignKey(userProfile, related_name='platform_update_user', verbose_name='修改人',on_delete=CASCADE)
    update_time = DateTimeField(verbose_name='修改时间', auto_now=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=((1, '正常'), (0, '停用')), default=1)

    class Meta:
        verbose_name = '平台用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.platform.name, self.username)





