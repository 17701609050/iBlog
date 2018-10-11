# -*- coding: UTF-8 -*-
import logging
import traceback
import json
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http.response import HttpResponseRedirect, HttpResponse
from django.template import TemplateDoesNotExist, RequestContext
# from .login_service import do_login
from apps.blog.search_blogs import searchblog
from apps.blog.views import Category1, Category2, __get_blog_info, __my_pagination, Blog
# @csrf_exempt
# def user_login(request):
#     if request.method == 'GET':
#         return render_to_response('common/login.html',  {}, RequestContext(request))
#     else:
#         res = {'result': 'error'}
#         response = HttpResponse()
#         try:
#             if request.POST.get('username') is not None:
#                 (result, s,) = do_login(request, True)
#                 res.update({'result': ('success' if result else 'fail')})
#         except Exception as e:
#             raise e
#         finally:
#             res.update({'user_token': request.session.session_key})
#             response.write(json.dumps(res).encode('utf-8'))
#             return response
#
# @csrf_exempt
# def user_logout(request):
#     # do something for logout
#     logout(request)
#     return render_to_response("common/logout.html", {}, RequestContext(request))


def search(request):
    search_key = request.GET.get('q', '')
    offset = request.GET.get('offset', '0')
    limit = request.GET.get('limit', '4')

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
    content = {
        # 'obj_infos': blogs,
        # 'obj_page_range': obj_page_range,
        'category1': category1,
        'category2': category2,
        'search_key': search_key,
        'offset': offset,
        'limit': limit,
    }
    return render_to_response('blog/search_blog_result.html', content, RequestContext(request))
