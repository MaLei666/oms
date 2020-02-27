# Generated by Django 2.0.6 on 2019-12-19 12:26

from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField
from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191217_2301'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=CharField(blank=True, max_length=500, null=True, verbose_name='居住地'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='users/avatar/default.png', max_length=200, null=True, upload_to='users/avatar/%Y/%m', verbose_name='用户头像'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='identifier',
            field=CharField(default=10, max_length=40, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=CharField(blank=True, max_length=100, null=True, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='电子邮件'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=CharField(max_length=100, verbose_name='登录账号'),
        ),
    ]
