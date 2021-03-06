# -*- coding: UTF-8 -*-
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
import sys
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TEMPLATES_DIRS = (
#     os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
#     )
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&1&-t%7=y@yn&7f33-4s)ok#qa%qmckxe!rwv57cqou0x2)+xj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

COMPRESS_ENABLED = True
ALLOWED_HOSTS = ['*']

# Application definition
# Django apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # 'django.contrib.sites',
)

# Third party apps
THIRD_PARTY_APPS = (
    'DjangoUeditor',
    'django_filters',
    'rest_framework',
    'rest_framework_swagger',
    'haystack',
    'xadmin',
    'crispy_forms',
    'ckeditor',
    'mptt',
)

# System api apps
API_APPS = (
    'apps.blog',
    'apps.resource',
    'apps.user',
    'apps.rest',
    'apps.movie',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + API_APPS

APPS_DIR = os.path.join(BASE_DIR, 'apps')
# Uninstall apps, api is hidden
UNINSTALL_APPS = ('__pycache__')
LOCAL_APPS = [o for o in os.listdir(APPS_DIR) if os.path.isdir(os.path.join(APPS_DIR, o)) and
              not o.startswith('.') and o not in UNINSTALL_APPS]

# AUTH_PROFILE_MODULE = 'user.Profile'

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'iBlog.middleware.SessionInterceptor',
)


ROOT_URLCONF = 'iBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'iBlog.context_processors.site_global_variable',

            ],
        },
    },
]

WSGI_APPLICATION = 'iBlog.wsgi.application'

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # drf的这一阶段主要是做验证,middleware的auth主要是设置session和user到request对象
        # 默认的验证是按照验证列表从上到下的验证
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    )
}


JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    # 'JWT_SECRET_KEY': settings.SECRET_KEY,
    # 'JWT_GET_USER_SECRET_KEY': None,
    # 'JWT_PUBLIC_KEY': None,
    # 'JWT_PRIVATE_KEY': None,
    # 'JWT_ALGORITHM': 'HS256',
    # 'JWT_VERIFY': True,
    # 'JWT_VERIFY_EXPIRATION': True,
    # 'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': '',

}

# haystack全文搜索配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'compressor.finders.CompressorFinder',
)

# github第三方登录配置
# 请求gihhub第三方登录url
GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_CLIENTID = '562508c3b735bbb0c0b4'
GITHUB_CLIENTSECRET = '15c2a5f79c6b75fdd1268944de733c3a74a439e5'

# 这里是github认证处理的url,就是自己处理登陆逻辑(被坑好好久)
GITHUB_CALLBACK = 'http://zipinglv.pythonanywhere.com/oauth/github/'

# 微博第三方认证
WEIBO_APP_ID = "3633532818"
WEIBO_APP_KEY = "d8d1576c7b5a8340fcf78868e9b52a7b"
WEIBO_CALLBACK = "http://zipinglv.pythonanywhere.com/oauth/weibo/"

QQ_APP_ID = '101780430'
QQ_KEY = '8eb5176485d562275b7b83bf4d37d1d3'
QQ_RECALL_URL = 'https://zipinglv.pythonanywhere.com/oauth/qq'


def get_current_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
# print get_current_host_ip()
if get_current_host_ip() == '172.19.232.246':  # '47.103.28.249'
    GITHUB_CLIENTID = '1974fa4300940b35ea71'
    GITHUB_CLIENTSECRET = '44cc84e8b7d4d5282aa5577f3aafd75e8b2d3407'
    GITHUB_CALLBACK = 'http://www.zipinglv.club/oauth/github/'

    WEIBO_APP_ID = "841152038"
    WEIBO_APP_KEY = "da0e6fb4eafc3b6a76c9662b2066d7ff"
    WEIBO_CALLBACK = 'http://www.zipinglv.club/oauth/weibo/'

    QQ_APP_ID = '101782337'
    QQ_KEY = '7c676a72bbd3913a82820007d81df9d9'
    QQ_RECALL_URL = 'http://www.zipinglv.club/oauth/qq'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
SESSION_ENGINE_ALIAS = 'redis'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'

FILE_CHARSET = 'utf-8'

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_ROOT=os.path.join(os.path.dirname(SITE_ROOT),'static').replace('\\','/')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# STATIC_ROOT=os.path.join(BASE_DIR, 'static').replace('\\','/')
STATIC_ROOT = '/var/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/var/media/')
MEDIA_DIRS = (
    os.path.join(BASE_DIR, '/var/media/')

)

CKEDITOR_CONFIGS = {

    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            # 在工具栏中添加该功能的按钮
            ['CodeSnippet'], ['Source'],

        ],
        'toolbar': 'Full',
        'height': 291,
        'width': '100%',
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
        # 添加的插件
        'extraPlugins': 'codesnippet',
    }
}

# --------------- 邮件配置 ------------------ #
SERVER_EMAIL = "17701609050@163.com"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = '17701609050@163.com'
DEFAULT_FROM_EMAIL = 'lvziping@163.com'  # 必须与EMAIL_HOST_USER保持一直不然报错553
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'LZP999102'
# 收件人看到的发件人
EMAIL_FROM = '<LvZiping@163.com>'


ADMINS = (
    ('zipingx', '459260276@qq.com'),
    ('zipinglv', '17701609050@163.com'),
)

# --------------- 邮件配置END ------------------ #

# --------------- logging setting ------------ #
LOG_PATH = os.path.join(BASE_DIR, 'log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {  # log format
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {  # filter
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {  # send an email to admin
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file_handler': {  # log to the file
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            # 'filename': os.path.join('/var/www/log', "autoHub", 'autoHubLog.txt'),  # log file
            'filename':  os.path.join(LOG_PATH, 'debug.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 50,
            'formatter': 'standard',  # log format
        },
        'console': {  # log to console
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {  # logging manager
        'django': {
            'handlers': ['console', 'file_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['file_handler', 'console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
