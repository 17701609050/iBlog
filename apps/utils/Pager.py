# -*- coding: UTF-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponse
from django.conf import settings


class Page(object):

    def page(self, objs, page):
        paginator = Paginator(objs, settings.REST_FRAMEWORK["PAGE_SIZE"])
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        try:
            objs = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            objs = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            objs = paginator.page(paginator.num_pages)
        return objs, paginator
