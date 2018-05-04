# -*- coding: utf-8 -*-

# Extend base setting
from iBlog.settings import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zipinglv$iblog',
        'USER': 'zipinglv',
        'PASSWORD': 'lzp17701609050',
        'HOST': 'zipinglv.mysql.pythonanywhere-services.com',
        'PORT': '3306'
    }
}