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
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Redis caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            # "SOCKET_TIMEOUT": 5,  # in seconds
        }
    },
}

# Redis caches for session
SESSION_ENGINE_ALIAS = 'redis'
SESSION_CACHE_TIMEOUT = 24 * 60 * 60
SESSION_ENGINE = 'apps.blog.redis_session'

SESSION_REDIS = {}
SESSION_REDIS_HOST = '127.0.0.1'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_SOCKET_TIMEOUT = 0.1
SESSION_REDIS_RETRY_ON_TIMEOUT = False
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = ''
SESSION_REDIS_PREFIX = 'icg-session'
SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = None
SESSION_REDIS_URL = None
SESSION_REDIS_POOL = None
SESSION_REDIS_SENTINEL_LIST = None
SESSION_REDIS_SENTINEL_MASTER_ALIAS = None
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
