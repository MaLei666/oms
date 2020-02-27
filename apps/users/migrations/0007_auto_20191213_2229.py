# Generated by Django 2.0.6 on 2019-12-13 22:29

from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField
from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191213_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdepartment',
            name='name',
            field=CharField(max_length=20, verbose_name='部门名称'),
        ),
        migrations.AlterUniqueTogether(
            name='userdepartment',
            unique_together={('unit', 'name')},
        ),
    ]
