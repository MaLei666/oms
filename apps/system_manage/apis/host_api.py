# #!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# # -*- coding:utf-8 -*-
# # @author : MaLei
# # @datetime : 2019-11-12 21:11
# # @file : host_api.py
# # @software : PyCharm
#
# from users.serializers import *
# from ..filter import *
# from utils.code_response import response_fomat
# from ..models import *
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import logout,authenticate
# from utils.commen_method import login_info,UserOperation
# from utils.login_check import LoginStatusCheck
# from django.views import View
# from users.forms import ChangeUserPasswordForm
# from operation_record.serializers import operaSerializer,UserOperationRecord
# ######################################
# # 第三方模块
# ######################################
# from rest_framework import status, generics, viewsets, renderers, permissions
# from rest_framework.response import Response
# from rest_framework_jwt.views import APIView
# from rest_framework.exceptions import PermissionDenied
#
# __all__ = ['osViewSet', 'unitViewSet', 'deptViewSet','logout_view','change_pw_view','logininfo_view',
#            'operation_record_view']
#
#
# class osViewSet(viewsets.ModelViewSet):
#     serializer_class =
#     queryset = UserCompany.objects.all().order_by('id')
#     filter_class = unitFilter
#     lookup_url_kwarg = 'unit_id'
#     code = response_fomat()
#
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_authenticated:
#             if user.role < 3:
#                 return self.queryset
#             else:
#                 return self.queryset.filter(id=user.unit_id)
#         else:
#             return self.code.authenticat_failed()
#
#     def create(self, request, *args, **kwargs):
#         if request.user.role < 3:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return Response(self.code.request_add_succeed(), status=status.HTTP_200_OK)
#         else:
#             return Response(self.code.no_permission())
#
#     def partial_update(self, request, *args, **kwargs):
#         if request.user.role < 3 or \
#                 (request.user.unit_id == kwargs['unit_id'] and request.user.role == 3):
#             kwargs['partial'] = True
#             self.update(request, *args, **kwargs)
#             return Response(self.code.request_edit_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#     def destroy(self, request, *args, **kwargs):
#         if request.user.role < 3:
#             instance = self.get_object()
#             unitSerializer().delete(request, instance)
#             self.perform_destroy(instance)
#             return Response(self.code.request_delete_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#
# class deptViewSet(viewsets.ModelViewSet):
#     serializer_class = deptSerializer
#     queryset = UserDepartment.objects.all().order_by('id')
#     filter_class = deptFilter
#     lookup_url_kwarg = 'dept_id'
#     code = response_fomat()
#
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_authenticated:
#             if user.role < 3:
#                 return self.queryset
#             elif user.role == 3:
#                 return self.queryset.filter(unit_id=user.unit_id)
#             else:
#                 return self.queryset.filter(id=user.dept_id)
#         else:
#             return self.code.authenticat_failed()
#
#     def create(self, request, *args, **kwargs):
#         if request.user.role < 3 or \
#                 (request.user.role == 3 and request.data['unit_id'] == request.user.unit_id):
#             if self.queryset.filter(unit_id=request.data['unit_id'], name=request.data['name']):
#                 return Response(self.code.duplicate_data())
#             serializer = self.get_serializer(data=request.data)
#             if not serializer.is_valid(raise_exception=True):
#                 return Response(serializer.errors)
#             self.perform_create(serializer)
#             return Response(self.code.request_add_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#     def partial_update(self, request, *args, **kwargs):
#         if request.user.role < 3 or \
#                 request.user.dept_id == self.kwargs['dept_id'] or \
#                 (request.user.role == 3 and request.user.unit_id == self.queryset.get(
#                     id=self.kwargs['dept_id']).unit_id):
#             try:
#                 self.queryset.get(unit_id=self.queryset.get(id=self.kwargs['dept_id']).unit_id,
#                                   name=request.data['name'])
#                 return Response(self.code.duplicate_data())
#             except:
#                 kwargs['partial'] = True
#                 self.update(request, *args, **kwargs)
#                 return Response(self.code.request_edit_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#     def destroy(self, request, *args, **kwargs):
#         if request.user.role < 3 or \
#                 (request.user.unit_id == self.queryset.get(
#                     id=self.kwargs['dept_id']).unit_id and request.user.role == 3):
#             instance = self.get_object()
#             deptSerializer().delete(request, instance)
#             self.perform_destroy(instance)
#             return Response(self.code.request_delete_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = userProfile.objects.all().order_by('id')
#     filter_class = UserFilter
#     lookup_url_kwarg = 'user_id'
#     code = response_fomat()
#
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_authenticated:
#             if user.role < 3:
#                 return self.queryset.filter(role__gte=user.role).order_by('id')
#             elif user.role == 3:
#                 return self.queryset.filter(unit_id=user.unit_id, role__gte=user.role)
#             else:
#                 return self.queryset.filter(dept_id=user.dept_id, role__gte=user.role)
#         return Response(self.code.authenticat_failed())
#
#     def create(self, request, *args, **kwargs):
#         if request.user.role < int(request.data.get('role')):
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return Response(self.code.request_add_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#     def partial_update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if request.user.id == kwargs['user_id'] or \
#                 (request.user.role < 3 and request.user.role < instance.role) or \
#                 (request.user.unit_id == instance.unit_id and request.user.role < instance.role) or \
#                 (request.user.dept_id == instance.dept_id and request.user.role < instance.role):
#             kwargs['partial'] = True
#             self.update(request, *args, **kwargs)
#             return Response(self.code.request_edit_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if (request.user.role < 3 and request.user.role < instance.role) or \
#                 (request.user.unit_id == instance.unit_id and request.user.role < instance.role) or \
#                 (request.user.dept_id == instance.dept_id and request.user.role < instance.role):
#             UserSerializer().delete(request, instance)
#             self.perform_destroy(instance)
#             return Response(self.code.request_delete_succeed())
#         else:
#             return Response(self.code.no_permission())
#
#
# ######################################
# # 登出
# ######################################
# class logout_view(APIView):
#     def get(self, request):
#         # 保存登录信息
#         login_info(2,
#                    request.user,
#                    request.META['HTTP_USER_AGENT'],
#                    request.META['REMOTE_ADDR'],
#                    request.user.address)
#
#         logout(request)
#
#         return Response(response_fomat().loginout_success())
#
# ######################################
# # 修改用户密码
# ######################################
# class change_pw_view(APIView):
#     def post(self, request):
#         change_user_password_form = ChangeUserPasswordForm(request.data)
#         if change_user_password_form.is_valid():
#             cur_password = request.data.get('cur_password')
#             new_password = request.data.get('new_password')
#             renew_password = request.data.get('renew_password')
#
#             if new_password != renew_password:
#                 return Response(response_fomat().password_discord())
#             elif authenticate(username=request.user.username, password=cur_password) is None:
#                 return Response(response_fomat().password_wrong())
#             else:
#                 request.user.password = make_password(new_password)
#                 request.user.save()
#                 # 添加操作记录
#                 UserOperation(op_user=request.user,
#                               username=request.user.username,
#                               user_name = request.user.user_name,
#                               role = request.user.role,
#                               unit_id = request.user.unit_id,
#                               unit_name = request.user.unit_name,
#                               dept_id = request.user.dept_id,
#                               dept_name = request.user.dept_name,
#                               belong=3,
#                               status=1,
#                               op_num=request.user.id,
#                               operation=2,
#                               action="用户 [ %s ] 修改了密码" % request.user.user_name)
#
#
#
#
#                 return Response(response_fomat().request_edit_succeed())
#         else:
#             return Response(response_fomat().data_illegal())
#
# ######################################
# # 用户登录信息查询
# ######################################
# class logininfo_view(APIView):
#     queryset=UserLoginInfo.objects.all().order_by('id')
#
#     def get(self,request):
#         try:
#             user = request.user
#             if user.is_authenticated:
#                 if user.role<3:
#                     info=self.queryset.filter(role__gte=user.role)
#                 elif user.role==3:
#                     info= self.queryset.filter(unit_id=user.unit_id, role__gte=user.role)
#                 elif user.role==4:
#                     info= self.queryset.filter(dept_id=user.dept_id, role__gte=user.role)
#                 else:
#                     info= self.queryset.filter(user_id=user.id).order_by('id')
#                 serializer = loginSerializer(info, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response(response_fomat().authenticat_failed())
#         except:
#             return Response(response_fomat().internal_server_error())
#
# ######################################
# # 用户操作查询
# ######################################
# class operation_record_view(APIView):
#     queryset=UserOperationRecord.objects.all().order_by('id')
#
#     def get(self,request):
#         try:
#             user = request.user
#             if user.is_authenticated:
#                 if user.role<3:
#                     info=self.queryset.filter(role__gte=user.role)
#                 elif user.role==3:
#                     info= self.queryset.filter(unit_id=user.unit_id, role__gte=user.role)
#                 elif user.role==4:
#                     info= self.queryset.filter(dept_id=user.dept_id, role__gte=user.role)
#                 else:
#                     info= self.queryset.filter(user_id=user.id).order_by('id')
#                 serializer = operaSerializer(info, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response(response_fomat().authenticat_failed())
#         except:
#             return Response(response_fomat().internal_server_error())
#
#
#
#
#
#
#
#
#
#
#
#
