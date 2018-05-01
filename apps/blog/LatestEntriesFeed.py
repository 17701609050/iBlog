# -*- coding:utf8 -*-
from django.contrib.syndication.views import Feed
from .models import Blog


class LatestEntriesFeed(Feed):
    title = u"刘文图熙1895"
    link = "blog.rocks"
    description = "关注刘文图熙1895的最新动态"

    def items(self):
        return Blog.objects.order_by('-pub_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return "/blog_detail/blog_" + str(item.id)
