# -*- coding: UTF-8 -*-
import xadmin
from xadmin import views
from .models import Blog, Category1, Category2, Tag, Profile, Profile_Tag, Friend, Friend_Tag


class BlogAdmin(object):
    list_display = ('title', 'pub_time', 'category1', 'category2', 'page_views')
    serch_field = ('category1', 'category2')
    list_filter = ('category1', 'category2')


class Category1Admin(object):
    list_display = ('category_1', 'display_name')


class Category2Admin(object):
    list_display = ('category_2', 'category1', 'display_name')


class ProfileAdmin(object):
    list_display = ('title', 'pub_time')


class FriendAdmin(object):
    list_display = ('name', 'friend_url')


xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Category1, Category1Admin)
xadmin.site.register(Category2, Category2Admin)
xadmin.site.register(Tag)
xadmin.site.register(Profile, ProfileAdmin)
xadmin.site.register(Profile_Tag)
xadmin.site.register(Friend, FriendAdmin)
xadmin.site.register(Friend_Tag)

# Register your models here.
