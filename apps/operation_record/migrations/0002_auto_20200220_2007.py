# Generated by Django 2.0.6 on 2020-02-20 20:07

from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField
from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroperationrecord',
            name='belong',
            field=PositiveSmallIntegerField(choices=[(1, '主机管理'), (2, '系统管理'), (3, '用户管理'), (4, '文档管理'), ((5, '巡检监督'), (6, '数据字典'))], verbose_name='归属'),
        ),
    ]
