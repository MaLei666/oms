#####################################
# Django 模块
######################################
from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField

######################################
# 自定义模块
######################################
from users.models import userProfile

__all__=['dataDictInfo','portToPortInfo','domainNameInfo','domainNameResolveInfo']

STATUS_CHOICES=(
    (0, '停用'),
    (1, '正常'),
    (2, '故障'),
)

######################################
# 端口映射表
######################################
class portToPortInfo(Model):
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    ip_out = GenericIPAddressField(verbose_name='公网 IP', null=True, blank=True)
    port_out = IntegerField(verbose_name='外网端口', null=True, blank=True)
    ip_in = GenericIPAddressField(verbose_name='内网 IP', null=True, blank=True)
    port_in = IntegerField(verbose_name='内网端口', null=True, blank=True)
    use = CharField(verbose_name='用途', max_length=20, null=True, blank=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '端口映射表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ("%s - %s") % (self.port_out, self.port_in)

######################################
# 域名表
######################################
class domainNameInfo(Model):
    name = CharField(verbose_name='名称', max_length=50)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '域名表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 域名解析表
######################################
class domainNameResolveInfo(Model):
    name = CharField(verbose_name='二级域名', max_length=20)
    ip = GenericIPAddressField(verbose_name='IP地址')
    domain_name_id = IntegerField(verbose_name='域名id',default=0)
    domain_name=CharField(verbose_name='域名', max_length=100, null=True, blank=True)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '域名解析表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s.%s' % (self.domain_name, self.name)

######################################
# 数据字典表
######################################
class dataDictInfo(Model):
    name =CharField(max_length=100,verbose_name='标签名',null=True,blank=True)
    value =CharField(max_length=100,verbose_name='数据值',null=True,blank=True)
    type =CharField(max_length=100,verbose_name='类型标志',null=True,blank=True)
    description =CharField(max_length=100,verbose_name='类型',null=True,blank=True)
    sort =DecimalField(max_digits=10,decimal_places=0,verbose_name='排序（升序)',null=True,blank=True)
    parent_id =BigIntegerField(null=True,blank=True,verbose_name='父级编号')
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment =CharField(max_length=255,verbose_name='备注信息',null=True,blank=True)

    class Meta:
        verbose_name = '数据字典表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s.%s' % (self.name,self.value)
