# -*- coding:utf8 -*-
from django.contrib.syndication.views import Feed
from .models import Blog


class LatestEntriesFeed(Feed):
    title = u"zipinglv个人博客"
    link = "blog.rocks"
    description = "ziping.lv的个人动态,与大家一起交流学习"

    def items(self):
        return Blog.objects.order_by('-pub_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return "/blog_detail/blog_" + str(item.id)
