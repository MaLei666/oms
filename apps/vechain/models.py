from django.db import models

######################################
# 产品表
######################################
class ArtifactInfo(models.Model):
    artifact_id = models.CharField(verbose_name='产品ID', max_length=255)
    id_status = models.IntegerField(verbose_name='ID状态')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    update_user = models.CharField(verbose_name='修改人',max_length=100, blank=True, null=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True, blank=True, null=True)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=((1, '正常'), (0, '停用')), default=1)


    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.artifact_id