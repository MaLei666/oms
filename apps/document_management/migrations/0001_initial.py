# Generated by Django 2.0.6 on 2019-08-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('belong', models.PositiveSmallIntegerField(choices=[(1, '文档'), (2, 'Shell脚本'), (3, 'Python脚本'), (4, 'Bat脚本'), (5, 'Bat脚本')], verbose_name='隶属')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (0, '停用')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '文档表',
                'verbose_name_plural': '文档表',
            },
        ),
        migrations.CreateModel(
            name='DocumentTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '分类表',
                'verbose_name_plural': '分类表',
            },
        ),
    ]
