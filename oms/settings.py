"""
Django settings for oms project.

*   为可选修改项目
**  为必须修改的项目

"""

import os, sys,datetime

######################################
# 兼容其他环境
######################################
import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True

######################################
# 配置相关目录
######################################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 自建APP
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# 第三方APP,xadmin
sys.path.insert(1, os.path.join(BASE_DIR, "extra_apps"))


######################################
# 安全配置
#####################################
SECRET_KEY = "2=x8z8e4psmp17sgdd@cripned2kj#jbuyz-wpam=c^p0$i^ew"

ALLOWED_HOSTS = ["*"]


######################################
# ** 数据库配置
######################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "oms",
        "USER": "root",
        "PASSWORD": "123456aa",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

######################################
# 定义 APP
######################################
INSTALLED_APPS = [
    "django.contrib.admin",
    "xadmin",
    "crispy_forms",
    "reversion",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    # "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    # users
    "users",
    # 分页
    "pure_pagination",
    # 主机管理
    "host_management",
    # 系统管理
    "system_manage",
    # 平台管理
    "platform_management",
    # 消息
    # "message",
    # 文档
    "document_management",
    # 操作记录
    "operation_record",
    # 线上管理
    # "online_management",
    # 爬虫数据
    "spider_data",
    #区块链
    "vechain",
    # 巡检监督
    "sys_inspect",
]


######################################
# REST_FRAMEWORK
######################################
REST_FRAMEWORK = {
    # Use Django"s standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PARSER_CLASSES":[
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # 用户登陆认证方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    "PAGE_SIZE": 10,
}

# jwt载荷中的有效期设置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1), # 有效期设置
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.login_check.jwt_response_payload_handler', #自定义token返回信息
}

######################################
# 中间件配置
######################################
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",    # 配置跨域中间件
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oms.urls"


######################################
# 模板配置
######################################
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")]
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Media 配置
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "oms.wsgi.application"
CORS_ORIGIN_ALLOW_ALL = True


######################################
# 认证配置
######################################
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# 定义认证模型
AUTH_USER_MODEL = "users.userProfile"

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = False


######################################
# 静态文件配置
######################################
STATIC_URL = "/static/"

# STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


######################################
# 上传文件配置
######################################
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")



######################################
# 分页规则
######################################
PAGINATION_SETTINGS = {
    # 中间部分显示的页码数
    "PAGE_RANGE_DISPLAYED": 5,
    # 前后页码数
    "MARGIN_PAGES_DISPLAYED": 2,
    # 是否显示第一页
    "SHOW_FIRST_PAGE_WHEN_INVALID": False,
}


######################################
# ** 系统地址
######################################
SERVER_URL = "http://localhost:8000"

# 远程服务部署的主机和端口
WEBSSH_IP = "localhost"
WEBSSH_PORT = "10001"



# session 设置
# 30分钟
SESSION_COOKIE_AGE = 60 * 30
SESSION_SAVE_EVERY_REQUEST = True
# 关闭浏览器，则COOKIE失效
SESSION_EXPIRE_AT_BROWSER_CLOSE = True




