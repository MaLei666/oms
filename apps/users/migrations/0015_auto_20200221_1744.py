# Generated by Django 2.0.6 on 2020-02-21 17:44

from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField
from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_delete_useremailvirificationcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogininfo',
            name='role',
            field=IntegerField(default=10, verbose_name='用户角色'),
        ),
        migrations.AddField(
            model_name='userlogininfo',
            name='username',
            field=CharField(default=1, max_length=200, verbose_name='用户名'),
            preserve_default=False,
        ),
    ]
