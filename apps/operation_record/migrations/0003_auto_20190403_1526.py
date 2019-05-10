# Generated by Django 2.0.6 on 2019-04-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_record', '0002_useroperationrecord_op_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroperationrecord',
            name='belong',
            field=models.PositiveSmallIntegerField(choices=[(1, '主机管理'), (2, '用户管理'), (3, '用户认证'), (4, '文档管理'), (5, '巡检设备')], verbose_name='归属'),
        ),
    ]
