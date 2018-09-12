# -*- coding: UTF-8 -*-
# coding=UTF-8

"""iBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from apps.rest.blog.viewsets import BlogView

router = DefaultRouter()

router.register(r'blogs', BlogView, 'blogs')

urlpatterns = [
    url(r'^blogs/$', BlogView.as_view({'get': 'list'})),

]
urlpatterns += router.urls

