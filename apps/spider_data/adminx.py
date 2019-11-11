# from django.contrib import admin
from .models import ZhihuInfo,ZhihuList,FoodRank,ShopInfo
import xadmin
# Register your models here.
xadmin.site.register(ZhihuInfo)
xadmin.site.register(ZhihuList)
xadmin.site.register(FoodRank)
xadmin.site.register(ShopInfo)