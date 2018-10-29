# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
import views

urlpatterns = [
   url(r'^github/$', views.github_auth, name='github_oauth'),
   url(r'^github_login/$', views.githhub_login, name='github_login'),
]
