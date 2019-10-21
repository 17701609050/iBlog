# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from . import github_oauth
from . import webo_oauth
from . import qq_oauth

urlpatterns = [
   url(r'^github/$', github_oauth.github_auth, name='github_oauth'),
   url(r'^github_login/(?P<targetUri>.*)$', github_oauth.githhub_login, name='github_login'),

   url(r'^weibo/$', webo_oauth.webo_auth, name='weibo_oauth'),  # 微博授权页面
   url(r'^weibo_login/(?P<targetUri>.*)$', webo_oauth.weibo_login, name='weibo_login'),  # 微博回调页面

   url(r'^qq/$', qq_oauth.qq_auth, name='qq_oauth'),  # 微博授权页面
   url(r'^qq_login/(?P<targetUri>.*)$', qq_oauth.qq_login, name='qq_login'),  # 微博回调页面
]
