# -*- coding: UTF-8 -*-
import logging
import traceback
import json
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import TemplateDoesNotExist, RequestContext
# from .login_service import do_login
from apps.blog.search_blogs import searchblog
from apps.blog.views import Category1, Category2, Tag, Friend, __get_blog_info, __my_pagination, Blog
from rest_framework_jwt.views import obtain_jwt_token
from apps.blog.models import Zan


def search(request):
    search_key = request.GET.get('q', '')
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', settings.REST_FRAMEWORK["PAGE_SIZE"])

    # pageindex = request.GET.get('page', '1')
    # 获取categoty1的所有分类,过滤出cate1的blog
    category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    cate1 = Category1.objects.get(category_1='study')

    category2 = Category2.objects.filter(category1_id=cate1)
    # blogs = searchblog.search_blogs(search_key)
    # blogs, obj_page_range = __my_pagination(request, blogs)
    # for blog in blogs:
    #     if len(blog['content'].encode('unicode-escape').decode('string_escape')) > 80:
    #         blog['content'] = blog['content'][0:80] + ' ...'
    #     else:
    #         blog['content'] = blog['content'][0:60]
    tags = Tag.objects.all()
    friends = Friend.objects.all()
    content = {
        # 'obj_infos': blogs,
        # 'obj_page_range': obj_page_range,
        'category1': category1,
        'category2': category2,
        'tags': tags,
        'friends': friends,
        'search_key': search_key,
        'offset': offset,
        'limit': limit,
    }
    return render(request, 'blog/search_blog_result.html', content)


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

