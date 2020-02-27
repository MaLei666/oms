from django.db.models import Model,CharField,DateTimeField,IntegerField,ForeignKey,FloatField,CASCADE

class FoodRank(Model):
    tip=CharField(verbose_name='排行类型', max_length=100)
    tip_id=IntegerField(verbose_name='排行类型id')
    classifi=CharField(verbose_name='店铺类型', max_length=100)
    rank_num=IntegerField(verbose_name='排名')
    shopId=CharField(verbose_name='店铺id', max_length=100)
    shopName=CharField(verbose_name='店铺名', max_length=100)
    mainRegionName=CharField(verbose_name='所在区域', max_length=100, blank=True, null=True)
    taste=FloatField(verbose_name='口味', blank=True, null=True)
    environment=FloatField(verbose_name='环境', blank=True, null=True)
    service=FloatField(verbose_name='服务', blank=True, null=True)
    avgPrice=IntegerField(verbose_name='平均消费', blank=True, null=True)
    city_id=IntegerField(verbose_name='城市id')
    address=CharField(verbose_name='地址', max_length=300, blank=True, null=True)
    update_time=DateTimeField(verbose_name='更新时间')

    class Meta:
        verbose_name = '大众点评店铺排行表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tip_id

class ShopInfo(Model):
    shopId=CharField(verbose_name='店铺id', max_length=100)
    shopName=CharField(verbose_name='店铺名称', max_length=100)
    review=CharField(verbose_name='评论', max_length=3000, blank=True, null=True)
    review_recommend=CharField(verbose_name='推荐菜', max_length=300, blank=True, null=True)
    review_time=DateTimeField(verbose_name='评论时间',max_length=300, blank=True, null=True)
    update_time=DateTimeField(verbose_name='更新时间',max_length=300, blank=True, null=True)
    now_page=IntegerField(verbose_name='页码')
    re_no=IntegerField(verbose_name='索引')

    class Meta:
        verbose_name = '大众点评店铺评论列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shopId


class ZhihuList(Model):
    question=CharField(verbose_name='问题标题', max_length=255)
    hot=CharField(verbose_name='问题热度', max_length=255)
    answer_count=IntegerField(verbose_name='回答数')


    class Meta:
        verbose_name = '知乎问题表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question

class ZhihuInfo(Model):

    question=ForeignKey(ZhihuList,to_field='id',verbose_name='问题标题',on_delete=CASCADE)
    text=CharField(verbose_name='回答内容', max_length=3000)
    author=CharField(verbose_name='回答作者', max_length=30)
    voteup_count=IntegerField(verbose_name='赞同数量', )
    comment_count=IntegerField(verbose_name='评论数量', )
    update_time=DateTimeField(verbose_name='更新时间', max_length=30)

    class Meta:
        verbose_name = '回答详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text