from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,ManyToManyField,DecimalField,BigIntegerField

######################################
# 产品表
######################################
class ArtifactInfo(Model):
    artifact_id = CharField(verbose_name='产品ID', max_length=255)
    id_status = IntegerField(verbose_name='ID状态')
    add_time = DateTimeField(verbose_name='添加时间', auto_now_add=True)
    update_user = CharField(verbose_name='修改人',max_length=100, blank=True, null=True)
    update_time = DateTimeField(verbose_name='修改时间', auto_now=True, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=((1, '正常'), (0, '停用')), default=1)


    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.artifact_id