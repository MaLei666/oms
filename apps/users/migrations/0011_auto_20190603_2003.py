# Generated by Django 2.0.6 on 2019-06-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190528_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '超级管理员'), (2, '平台管理员'), (3, '单位管理员'), (4, '一般用户')], null=True, verbose_name='角色'),
        ),
    ]
