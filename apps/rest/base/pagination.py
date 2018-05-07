# -*- coding: utf-8 -*-
"""
@Created on 2017-12-05
@Author: gaobo.xiao
@Version V1.0
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ICGGridPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'data': data
        })

