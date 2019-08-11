# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as resource_view

urlpatterns = [
   url(r'^$', resource_view.ResourceView.as_view(), name='resource'),
   url(r'^tag/tag_(?P<tag_id>\d+)/$', resource_view.ResourceView.as_view(), name='resource_tags'),
   url(r'^category/category_(?P<category_id>\d+)/$', resource_view.ResourceView.as_view(), name='resource_category'),
]
