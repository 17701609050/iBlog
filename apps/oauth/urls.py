# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
import github_oauth
import webo_oauth

urlpatterns = [
   url(r'^github/$', github_oauth.github_auth, name='github_oauth'),
   url(r'^github_login/$', github_oauth.githhub_login, name='github_login'),

   url(r'^weibo/$', webo_oauth.webo_auth, name='weibo_oauth'),  # 微博授权页面
   url(r'^weibo_login/$', webo_oauth.weibo_login, name='weibo_login'),  # 微博回调页面
]
