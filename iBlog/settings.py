#-*- coding: UTF-8 -*-
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

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
    'django.contrib.sitemaps',
    'DjangoUeditor',
    'haystack',
    'apps.blog',
    # 'compressor',

)

APPS_DIR = os.path.join(BASE_DIR, 'apps')
# Uninstall apps, api is hidden
UNINSTALL_APPS = ()
LOCAL_APPS = [o for o in os.listdir(APPS_DIR) if os.path.isdir(os.path.join(APPS_DIR, o)) and
              not o.startswith('.') and o not in UNINSTALL_APPS]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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

            ],
        },
    },
]



WSGI_APPLICATION = 'iBlog.wsgi.application'

# haystack全文搜索配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iblog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '3306'
    }
}

STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
        # 'compressor.finders.CompressorFinder',
)


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

DEFAULT_CHARSET = 'utf-8'

FILE_CHARSET = 'utf-8'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_ROOT=os.path.join(os.path.dirname(SITE_ROOT),'static').replace('\\','/')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# STATIC_ROOT=os.path.join(BASE_DIR, 'static').replace('\\','/')
#STATIC_ROOT='/var/www/blog/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# print STATIC_ROOT




