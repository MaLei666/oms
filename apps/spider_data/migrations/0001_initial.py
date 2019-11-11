# Generated by Django 2.0.6 on 2019-11-05 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(max_length=100, verbose_name='排行类型')),
                ('tip_id', models.IntegerField(verbose_name='排行类型id')),
                ('classifi', models.CharField(max_length=100, verbose_name='店铺类型')),
                ('rank_num', models.IntegerField(verbose_name='排名')),
                ('shopId', models.CharField(max_length=100, verbose_name='店铺id')),
                ('shopName', models.CharField(max_length=100, verbose_name='店铺名')),
                ('mainRegionName', models.CharField(blank=True, max_length=100, null=True, verbose_name='所在区域')),
                ('taste', models.FloatField(blank=True, null=True, verbose_name='口味')),
                ('environment', models.FloatField(blank=True, null=True, verbose_name='环境')),
                ('service', models.FloatField(blank=True, null=True, verbose_name='服务')),
                ('avgPrice', models.IntegerField(blank=True, null=True, verbose_name='平均消费')),
                ('city_id', models.IntegerField(verbose_name='城市id')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='地址')),
                ('update_time', models.DateField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '大众点评店铺排行表',
                'verbose_name_plural': '大众点评店铺排行表',
            },
        ),
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopId', models.CharField(max_length=100, verbose_name='店铺id')),
                ('shopName', models.CharField(max_length=100, verbose_name='店铺名称')),
                ('review', models.CharField(blank=True, max_length=3000, null=True, verbose_name='评论')),
                ('review_recommend', models.CharField(blank=True, max_length=300, null=True, verbose_name='推荐菜')),
                ('review_time', models.DateTimeField(blank=True, max_length=300, null=True, verbose_name='评论时间')),
                ('update_time', models.DateTimeField(blank=True, max_length=300, null=True, verbose_name='更新时间')),
                ('now_page', models.IntegerField(verbose_name='页码')),
                ('re_no', models.IntegerField(verbose_name='索引')),
            ],
            options={
                'verbose_name': '大众点评店铺评论列表',
                'verbose_name_plural': '大众点评店铺评论列表',
            },
        ),
        migrations.CreateModel(
            name='ZhihuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=3000, verbose_name='回答内容')),
                ('author', models.CharField(max_length=30, verbose_name='回答作者')),
                ('voteup_count', models.IntegerField(verbose_name='赞同数量')),
                ('comment_count', models.IntegerField(verbose_name='评论数量')),
                ('update_time', models.DateTimeField(max_length=30, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '回答详情',
                'verbose_name_plural': '回答详情',
            },
        ),
        migrations.CreateModel(
            name='ZhihuList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='问题标题')),
                ('hot', models.CharField(max_length=255, verbose_name='问题热度')),
                ('answer_count', models.IntegerField(verbose_name='回答数')),
            ],
            options={
                'verbose_name': '知乎问题表',
                'verbose_name_plural': '知乎问题表',
            },
        ),
        migrations.AddField(
            model_name='zhihuinfo',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spider_data.ZhihuList', verbose_name='问题标题'),
        ),
    ]