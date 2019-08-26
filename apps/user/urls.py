# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
import views

urlpatterns = [
   url(r'^login/$', views.user_login, name='login'),
   url(r'^sign_up/$', views.user_sign_up, name='sign_up'),
   url(r'^logout/$', views.user_logout, name='logout'),
]
