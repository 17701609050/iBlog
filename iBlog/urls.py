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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap, index

from .settings import LOCAL_APPS
from apps.blog.sitemap import sitemaps
from apps.blog.LatestEntriesFeed import LatestEntriesFeed

import apps.blog.views as blog_views

urlpatterns = [
    url(r'^$', blog_views.index, name='index'),
    url(r'^profile/$', blog_views.profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/img/favicon-defalt.ico')),
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^feed/main\.xml$', LatestEntriesFeed()),
]
# Auto-add the applications.
for app in LOCAL_APPS:
    urlpatterns += patterns('', url(r'^{0}/'.format(app), include('apps.' + app + '.urls')), )  # without namespace
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
