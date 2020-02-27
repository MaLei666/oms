# Generated by Django 2.0.6 on 2020-02-27 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_add_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
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
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(to='document_management.DocumentTags', verbose_name='分类标签'),
        ),
        migrations.AddField(
            model_name='document',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
    ]
