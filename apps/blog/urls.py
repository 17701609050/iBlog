# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as blog_view

urlpatterns = [
   url(r'^(?P<blog_url>\w+)/$', blog_view.blog_index, name='blog_index'),
   url(r'^blog_detail/blog_(?P<blog_id>\d+)/$', blog_view.blog_detail, name='blog_detail'),
   url(r'^tag/tag_(?P<tag_id>\d+)/$', blog_view.tag, name='tag'),
   url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

   url(r'^post-comment/(?P<blog_id>\d+)/$', blog_view.post_comment, name='post_comment'),
   url(r'^post-comment/(?P<blog_id>\d+)/(?P<parent_comment_id>\d+)/$', blog_view.post_comment, name='comment_reply')
]
