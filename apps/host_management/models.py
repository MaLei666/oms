#####################################
# Django 模块
######################################
from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField

######################################
# 自定义模块
######################################
from users.models import userProfile

__all__=['operatingSystemInfo','projectInfo','useInfo','hostInfo','hostServiceInfo','databaseInfo',
         'databaseDBInfo','idcInfo','rackInfo']

STATUS_CHOICES=(
    (0, '停用'),
    (1, '正常'),
    (2, '故障'),
)
######################################
# 操作系统表
######################################
class operatingSystemInfo(Model):
    name = CharField(verbose_name='系统名称', max_length=30,unique=True)
    version = CharField(verbose_name='系统版本', max_length=10, blank=True, null=True)
    bit = PositiveSmallIntegerField(verbose_name='位数', choices=((32, '32位'), (64, '64位')),blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)
    comment= CharField(verbose_name='描述', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = '操作系统'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

######################################
# 项目表
######################################
class projectInfo(Model):
    name = CharField(verbose_name='项目名称', max_length=30)
    op_user = CharField(verbose_name='运维人员',max_length=200,blank=True, null=True)
    run_env = CharField(verbose_name='运行环境', max_length=100, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)
    comment= CharField(verbose_name='描述', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

######################################
# 用途表
######################################
class useInfo(Model):
    name = CharField(verbose_name='用途', max_length=30,unique=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    comment= CharField(verbose_name='描述', max_length=200, blank=True, null=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '用途'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

######################################
# 机房表
######################################
class idcInfo(Model):
    name=CharField(verbose_name='名称',max_length=100)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    isp = CharField(max_length=200, verbose_name="运营商", blank=True, null=True)
    line = CharField(max_length=200, verbose_name="运营商线路", blank=True, null=True)
    bandwidth = CharField(max_length=200, verbose_name="机房出口带宽", blank=True, null=True)
    racks = IntegerField(default=0, verbose_name="机柜个数", blank=True, null=True)
    address = CharField(verbose_name='位置', max_length=200, blank=True, null=True)
    connect = CharField(verbose_name='联系人', max_length=30, blank=True, null=True)
    connect_phone=CharField(verbose_name='机房联系电话',max_length=30, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

######################################
# 机柜表
######################################
class rackInfo(Model):
    name=CharField(verbose_name='名称',max_length=100)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    idc_id = BigIntegerField(verbose_name="机房id")
    idc_name = CharField(verbose_name="机房名称",max_length=100, null=True, blank=True)
    number = BigIntegerField(blank=True, null=True, verbose_name="机柜号")
    height = BigIntegerField(blank=True, null=True, verbose_name="机柜高度")
    power = BigIntegerField(blank=True, null=True, verbose_name="机柜电力")
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)


######################################
# 主机信息表
######################################
class hostInfo(Model):
    hostname = CharField(verbose_name='主机名', max_length=30)
    in_ip = GenericIPAddressField(verbose_name='内网IP')
    out_ip = GenericIPAddressField(verbose_name='外网IP', blank=True, null=True)
    system = CharField(verbose_name='操作系统', max_length=100,blank=True, null=True)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    idc_id = IntegerField(verbose_name="机房id", null=True, blank=True)
    idc_name = CharField(verbose_name=" 机房名称", max_length=30, null=True, blank=True)
    rack_id = IntegerField(verbose_name="机柜id", null=True, blank=True)
    rack_name = CharField(verbose_name="机柜名称", max_length=30, null=True, blank=True)
    address = CharField(verbose_name='具体位置', max_length=200, null=True, blank=True)
    disk = IntegerField(verbose_name='磁盘',blank=True, null=True)
    memory = IntegerField(verbose_name='内存',blank=True, null=True)
    network = IntegerField(verbose_name='带宽', blank=True, null=True)
    ssh_port = IntegerField(verbose_name='远程端口',null=True)
    root_ssh = BooleanField(verbose_name='是否允许 root 远程', default=True)
    use = CharField(verbose_name='用途', max_length=200, blank=True, null=True)
    project = CharField(verbose_name='项目', max_length=200, blank=True, null=True)
    admin_user = CharField(verbose_name='管理员用户', max_length=20, blank=True, null=True)
    admin_pass = CharField(verbose_name='管理员密码', max_length=50, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '主机信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.in_ip


######################################
# 服务信息表
######################################
class hostServiceInfo(Model):
    host_id = IntegerField(verbose_name='主机id')
    hostname = CharField(verbose_name='主机名', max_length=30)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    name = CharField(verbose_name='服务名称', max_length=30)
    version = CharField(verbose_name='服务版本', max_length=20, blank=True, null=True)
    listen_user = CharField(verbose_name='监听用户', max_length=20)
    listen_port = CharField(verbose_name='监听端口', max_length=30)
    ins_path = CharField(verbose_name='安装路径', max_length=100)
    log_path = CharField(verbose_name='日志路径', max_length=100, blank=True, null=True)
    backup_path = CharField(verbose_name='备份路径', max_length=100, blank=True, null=True)
    start_cmd = CharField(verbose_name='启动命令', max_length=100)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '主机服务信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 数据库服务
######################################
class databaseInfo(Model):
    host = ForeignKey(hostInfo, verbose_name='主机', related_name='db_host', on_delete=CASCADE)
    hostname = CharField(verbose_name='主机名', max_length=30)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    db_name = CharField(verbose_name='数据库名称', max_length=20, blank=True, null=True)
    db_version = CharField(verbose_name='数据库版本', max_length=20, blank=True, null=True)
    db_admin_user = CharField(verbose_name='数据库管理员', max_length=20)
    db_admin_pass = CharField(verbose_name='数据库管理员密码', max_length=50)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    comment= CharField(verbose_name='备注', max_length=200, blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '数据库服务信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.host.in_ip


######################################
# 数据库
######################################
class databaseDBInfo(Model):
    db = ForeignKey(databaseInfo, verbose_name='数据库', related_name='db_db_db', on_delete=CASCADE)
    unit_id = IntegerField(verbose_name='单位ID', null=True, blank=True)
    unit_name = CharField(verbose_name='单位名称', max_length=100, null=True, blank=True)
    dept_id = IntegerField(verbose_name='部门ID', null=True, blank=True)
    dept_name = CharField(verbose_name='部门名称', max_length=100, null=True, blank=True)
    name = CharField(verbose_name='库名', max_length=20)
    use = CharField(verbose_name='用途', max_length=20, null=True, blank=True)
    comment= CharField(verbose_name='备注', max_length=100, blank=True, null=True)
    user_id_create = BigIntegerField(verbose_name='创建用户id', null=True, blank=True)
    create_user = CharField(verbose_name='创建者', max_length=45, null=True, blank=True)
    create_time = DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    update_user = CharField(verbose_name='更新者', max_length=45, blank=True, null=True)
    update_time = DateTimeField(verbose_name='更新时间', blank=True, null=True)
    status = PositiveSmallIntegerField(verbose_name='状态', choices=(STATUS_CHOICES), default=1)

    class Meta:
        verbose_name = '数据库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ("%s - %s") % (self.db.db_name, self.name)
