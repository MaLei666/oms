# Generated by Django 2.0.6 on 2020-02-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrank',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间'),
        ),
    ]
