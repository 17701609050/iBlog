# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as blog_view

urlpatterns = [
   url(r'^blog_detail/blog_(?P<blog_id>\d+)/$', blog_view.blog_detail, name='blog_detail'),
   url(r'^tag_(?P<tag_id>\d+)/$', blog_view.tag, name='tag'),
   url(r'^geek/$', blog_view.geek, name='geek'),
   url(r'^essay/$', blog_view.essay, name='essay'),
   url(r'^joke/$', blog_view.joke, name='joke'),
   url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

]
