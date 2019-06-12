######################################
# Django 模块
######################################
from django.db import models
from django.db.models import Q

######################################
# 系统模块
######################################
import datetime

######################################
# 自定义模块
######################################
from users.models import UserProfile,UserDepartment,UserCompany


######################################
# 巡检设备表
######################################
class InspectDevInfo(models.Model):
    platform_id =models.CharField(max_length=45,blank=True,null=True,verbose_name='平台ID')
    dept_id =models.BigIntegerField(verbose_name='部门ID',blank=True,null=True)
    dept_name =models.CharField(max_length=100,blank=True,null=True,verbose_name='部门名称')
    unit_id =models.BigIntegerField(blank=True,null=True,verbose_name='部门ID')
    unit_name=models.CharField(max_length=100,blank=True,null=True,verbose_name='单位名称')
    unit_address=models.CharField(max_length=255,blank=True,null=True,verbose_name='单位地址')
    dev_id =models.CharField(max_length=255,verbose_name='设备ID',unique=True)
    dev_name =models.CharField(max_length=255,verbose_name='设备名称')
    dev_type =models.CharField(max_length=255,blank=True,null=True,verbose_name='巡检设备类型')
    dev_status = models.IntegerField(verbose_name='设备状态',default=1)
    install_position=models.CharField(max_length=255,blank=True,null=True,verbose_name='安装位置')
    create_time=models.DateTimeField(verbose_name='创建时间')
    update_time =models.DateTimeField(verbose_name='更新时间',blank=True,null=True)
    update_user =models.CharField(max_length=255,blank=True,null=True,verbose_name='更新者')
    create_user =models.IntegerField(verbose_name='创建用户')
    create_mobile =models.CharField(max_length=255,blank=True,null=True,verbose_name='创建用户手机号')
    comment =models.CharField(max_length=1000,verbose_name='备注',blank=True,null=True)
    msg_id =models.CharField(max_length=100,blank=True,null=True,verbose_name='信息ID')
    dev_image1 =models.CharField(max_length=255,blank=True,null=True,verbose_name='设备图片')
    dev_image2 =models.CharField(max_length=255,blank=True,null=True,verbose_name='设备图片')
    dev_image3 =models.CharField(max_length=255,blank=True,null=True,verbose_name='设备图片')
    type1 =models.IntegerField(blank=True,null=True,verbose_name='设备分类1')
    type2 =models.IntegerField(blank=True,null=True,verbose_name='设备分类2')
    type3 =models.IntegerField(blank=True,null=True,verbose_name='设备分类3')
    last_user_id =models.BigIntegerField(blank=True,null=True,verbose_name='最后修改者ID')
    last_user_name =models.CharField(max_length=45,blank=True,null=True,verbose_name='最后修改者名字')
    last_task_id =models.BigIntegerField(blank=True,null=True,verbose_name='最后任务ID')
    last_task_no =models.CharField(max_length=100,blank=True,null=True,verbose_name='最后任务no')
    last_task_name=models.CharField(max_length=200,blank=True,null=True,verbose_name='最后任务名称')
    last_task_time =models.DateTimeField(verbose_name='最后任务时间',blank=True,null=True)
    prev_user_id =models.BigIntegerField(blank=True,null=True,verbose_name='之前修改者ID')
    prev_user_name =models.CharField(max_length=45,blank=True,null=True,verbose_name='之前修改者名字')
    prev_task_id =models.BigIntegerField(blank=True,null=True,verbose_name='之前任务ID')
    prev_task_no =models.CharField(max_length=100,blank=True,null=True,verbose_name='之前任务no')
    prev_task_name =models.CharField(max_length=200,blank=True,null=True,verbose_name='之前任务名称')
    prev_task_time =models.DateTimeField(verbose_name='之前任务时间',blank=True,null=True)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=((1, '正常'), (0, '停用')), default=1)

    class Meta:
        verbose_name = '巡检设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dev_id


######################################
# 巡检任务表
######################################
class InspectContentInfo(models.Model):

    # content_no =models.CharField(max_length=45,verbose_name='内容编号')
    platform_id =models.CharField(max_length=45,verbose_name='平台ID',blank=True,null=True),
    dept_id =models.BigIntegerField(blank=True,null=True)
    dept_name =models.CharField(max_length=100,blank=True,null=True,verbose_name='部门名称')
    unit_id =models.BigIntegerField(blank=True,null=True)
    unit_name=models.CharField(max_length=100,blank=True,null=True,verbose_name='单位名称')
    user_id =models.BigIntegerField(blank=True,null=True)
    user_name =models.CharField(max_length=10,verbose_name='用户名称',blank=True,null=True)
    task_name =models.CharField(max_length=45,verbose_name='任务名称')
    task_type =models.IntegerField(verbose_name='任务类型')
    start_time =models.DateTimeField(verbose_name='开始时间')
    end_time =models.DateTimeField(verbose_name='结束时间')
    create_time =models.DateTimeField(auto_now=True,verbose_name='创建时间')
    update_time =models.DateTimeField(blank=True,null=True,verbose_name='更新时间')
    update_user =models.CharField(max_length=25,verbose_name='更新者',blank=True,null=True)
    create_user =models.CharField(max_length=25,verbose_name='创建用户',blank=True,null=True)
    comment =models.CharField(max_length=10,verbose_name='备注',blank=True,null=True)
    type1 =models.IntegerField(blank=True,null=True,verbose_name='执行模式')
    type2 =models.IntegerField(blank=True,null=True,verbose_name='设备分类2')
    type3 =models.IntegerField(blank=True,null=True,verbose_name='设备分类3')
    name1 =models.CharField(max_length=25,verbose_name='名称1',blank=True,null=True)
    name2 =models.CharField(max_length=25,verbose_name='名称2',blank=True,null=True)
    name3 =models.CharField(max_length=25,verbose_name='名称3',blank=True,null=True)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=((1, '正常'), (0, '停用')), default=1)

    class Meta:
        verbose_name = '巡检任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id





