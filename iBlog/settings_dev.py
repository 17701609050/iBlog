# -*- coding: utf-8 -*-

# Extend base setting
from iBlog.settings import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iblog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Redis caches
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#             # "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
#             # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
#             # "SOCKET_TIMEOUT": 5,  # in seconds
#         }
#     },
# }
#
# # Redis caches for session
# SESSION_ENGINE_ALIAS = 'redis'
# SESSION_CACHE_TIMEOUT = 24 * 60 * 60
# SESSION_ENGINE = 'apps.blog.redis_session'
#
# SESSION_REDIS = {}
# SESSION_REDIS_HOST = '127.0.0.1'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_SOCKET_TIMEOUT = 0.1
# SESSION_REDIS_RETRY_ON_TIMEOUT = False
# SESSION_REDIS_DB = 0
# SESSION_REDIS_PASSWORD = ''
# SESSION_REDIS_PREFIX = 'icg-session'
# SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = None
# SESSION_REDIS_URL = None
# SESSION_REDIS_POOL = None
# SESSION_REDIS_SENTINEL_LIST = None
# SESSION_REDIS_SENTINEL_MASTER_ALIAS = None
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_CLIENTID = '173bfda13180b1bf9fb2'
GITHUB_CLIENTSECRET = 'c262e8debfbc9f704b4d94bf40ffb52bc97683cb'

# 这里是github认证处理的url,就是自己处理登陆逻辑(被坑好好久)
GITHUB_CALLBACK = 'http://zipinglx.sh.intel.com:8081/oauth/github/'

WEIBO_APP_ID = "4084172258"
WEIBO_APP_KEY = "634304cdff7b812ebffd4fb53cf811eb"
WEIBO_CALLBACK = "http://zipinglx.sh.intel.com:8081/oauth/weibo/"


# OAuth设置
QQ_APP_ID = '101780430'
QQ_KEY = '8eb5176485d562275b7b83bf4d37d1d3'
QQ_RECALL_URL = 'https://zipinglv.pythonanywhere.com/oauth/qq'

SERVER_EMAIL = "auto-hub-site-report@intel.com"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.intel.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = '17701609050@163.com'
# #在邮箱中设置的客户端授权密码
# EMAIL_HOST_PASSWORD = 'lzp7230823w'
DEFAULT_FROM_EMAIL = 'auto-hub-site@intel.com'
ROBOT_ACCOUNT_EMAIL = '17701609050@163.com'

ADMINS = (
    ('zipingx', 'zipingx.lv@intel.com'),
    ('zipinglv', '17701609050@163.com'),
)

