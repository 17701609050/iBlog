# -*- coding: UTF-8 -*-
import logging
import traceback
import json
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from django.db.models import Count, Q
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import TemplateDoesNotExist, RequestContext
# from .login_service import do_login
from apps.blog.search_blogs import searchblog
from apps.blog.views import Category1, Category2, Tag, Friend, __get_blog_info, __my_pagination, __get_latest, Blog
from rest_framework_jwt.views import obtain_jwt_token
from apps.blog.models import Zan


def search(request):
    search_key = request.GET.get('search_key', '')
    # 获取categoty1的所有分类,过滤出cate1的blog
    category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    blogs_list = Blog.objects.all()
    obj_infos_all = blogs_list.filter(Q(title__contains=search_key) |
                                      Q(brief__contains=search_key) |
                                      Q(content__contains=search_key))


    obj_infos_all = __get_blog_info(obj_infos_all, None, None)
    obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)
    # 获取最新 blogs
    obj_latest = __get_latest(blogs_list)

    # 获取所有tag
    tags = Tag.objects.all()
    # 获取外链
    friends = Friend.objects.all()

    content = {
        'obj_infos': obj_infos,
        'obj_page_range': obj_page_range,
        'obj_latest': obj_latest,
        'category1': category1,
        # 'category2': category2,
        'tags': tags,
        'friends': friends,
        'search_key': search_key
    }

    return render(request, 'blog/blog_index.html', content)


def zan(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip_address = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip_address = request.META['REMOTE_ADDR']
    num = Zan.objects.update_or_create(ip_address=ip_address)
    zan_count = 3218 + Zan.objects.all().count()
    if num:
        return JsonResponse({"num": zan_count})
    else:
        return JsonResponse({"error": ''})

