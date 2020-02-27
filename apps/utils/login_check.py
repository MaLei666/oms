######################################
# Django 模块
######################################
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .code_response import response_fomat
from .commen_method import UserOperation,login_info

######################################
# 用户是否登录检测
######################################
class LoginStatusCheck(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginStatusCheck, self).dispatch(request, *args, **kwargs)



def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    :token  返回的jwt
    :user   当前登录的用户信息[对象]
    :request 当前本次客户端提交过来的数据
    """
    if user.status==1:

        # 保存登录信息
        login_info(1,
                   user,
                   user.username,
                   user.user_name,
                   user.role,
                   user.unit_id,
                   user.unit_name,
                   user.dept_id,
                   user.dept_name,
                   request.META['HTTP_USER_AGENT'],
                   request.META['REMOTE_ADDR'],
                   user.address)

        return {
            'token': token,
            'id': user.id,
            'username': user.username,
        }

    elif user.status==0:
        return response_fomat().status_outage()

    else:
        return response_fomat().status_abnormal()





