#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-12 20:57
# @file : serializers.py
# @software : PyCharm

from .models import *
from rest_framework import serializers

__all__=('UserSerializer',)
#TODO
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = '__all__'
        # fields=['url','password','last_login','is_superuser','username','first_name','last_name','email','is_staff',
        #         'is_active','date_joined','role','user_name','unit_id','unit_name','dept_id','dept_name','mobile',
        #         'avatar','gender','create_user','create_time','update_user','update_time','comment','status'
        #         ,'user_id_create']

    #
    # role = serializers.ChoiceField(choices=ROLE_CHOICES, required=False)
    # user_name = serializers.CharField(max_length=10)
    # unit_id = serializers.IntegerField(required=False)
    # unit_name = serializers.CharField(max_length=100, required=False)
    # dept_id = serializers.IntegerField(required=False)
    # dept_name = serializers.CharField(max_length=100, required=False)
    # mobile = serializers.CharField( max_length=20, required=False)
    # avatar = serializers.ImageField(max_length=200,default='users/avatar/default.png', required=False)
    # gender = serializers.ChoiceField(choices=GENDER_CHOICES, default='1', required=False)
    # email = serializers.EmailField(required=False)
    # # position = serializers.ForeignKey(UserPosition, on´_delete=serializers.CASCADE, required=False)
    # user_id_create = serializers.IntegerField(required=False)
    # create_user = serializers.CharField( max_length=45, required=False)
    # update_user = serializers.CharField( max_length=45, required=False)
    # comment = serializers.CharField(max_length=200, required=False)
    # status = serializers.ChoiceField(choices=STATUS_CHOICES, default=1)
    # is_staff = serializers.BooleanField(default=False)

    def create(self, validated_data):
        obj = super(UserSerializer, self).create(validated_data=validated_data)
        obj.save()
        return obj

    def update(self, instance, validated_data):
        instance.user_name=validated_data.get('user_name',instance.user_name)
        instance.mobile=validated_data.get('mobile',instance.mobile)
        instance.avatar=validated_data.get('avatar',instance.avatar)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.comment=validated_data.get('comment',instance.comment)
        instance.status=validated_data.get('user_name',instance.status)
        instance.email=validated_data.get('email',instance.email)
        instance.is_staff=validated_data.get('is_staff',instance.is_staff)
        instance.update_user=validated_data.user.user_name

        instance.save()
        return instance


class UserInfoSerializer(UserSerializer):
    class Meta:
        model=UserProfile
        fields = ['password', 'last_login', 'is_superuser', 'username', 'email', 'is_staff','date_joined','role',
                  'user_name','unit_id','unit_name','dept_id','dept_name','mobile','avatar','gender','create_user',
                  'create_time','update_user','update_time','comment','status','user_id_create']


#
# ######################################
# # 用户列表
# ######################################
# class UserListView(LoginStatusCheck, View):
#     def get(self, request):
#         # 页面选择
#         web_chose_left_1 = 'user_management'
#         web_chose_left_2 = 'user_list'
#         web_chose_middle = ''
#
#         # 用户
#         users = UserProfile.objects.all()
#         units=UserCompany.objects.all()
#         depts=UserDepartment.objects.all()
#
#         # 用户选择
#         user_check = request.GET.get('user_check', 'all')
#
#         # 正常
#         if user_check == 'up':
#             users = users.filter(status=1)
#
#         # 停用
#         if user_check == 'down':
#             users = users.filter(status=2)
#
#         # 男性
#         if user_check == '1':
#             users = users.filter(gender='2')
#
#         # 女性
#         if user_check == '1':
#             users = users.filter(gender='2')
#
#         # 查询
#         keyword = request.GET.get('keyword', '')
#
#         if keyword != '':
#             users = users.filter(
#                 Q(username__icontains=keyword) | Q(email__icontains=keyword) | Q(user_name__icontains=keyword)
#                 | Q(mobile__icontains=keyword) )
#
#         # 判断页码
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1
#
#         # 对取到的数据进行分页，记得定义每页的数量
#         p = Paginator(users, 12, request=request)
#
#         # 分页处理后的 QuerySet
#         users = p.page(page)
#
#         context = {
#             'web_chose_left_1': web_chose_left_1,
#             'web_chose_left_2': web_chose_left_2,
#             'web_chose_middle': web_chose_middle,
#             'users': users,
#             'units':units,
#             'depts':depts,
#             'user_check': user_check,
#             'keyword': keyword,
#         }
#         return render(request, 'users/units/user_list.html', context=context)
