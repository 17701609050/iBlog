# -*- coding: UTF-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from apps.rest.base.mixins import *
from apps.rest.blog.serializers import *
from apps.blog.models import Blog


class BlogView(MultipleFieldLookupMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('id', 'title', 'pub_time', 'brief', 'content', 'page_views')
    search_fields = ('id', 'title', 'brief', 'content', 'page_views')
    ordering = ('-pub_time')

    def get_serializer_class(self):
        return BlogViewSerializer

    @list_route(methods=['GET'])
    def get_blogs(self, request, *args, **kwargs):
        Blogs = Blog.objects.all()
        page = self.paginate_queryset(Blogs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(Blogs, many=True)
        return Response(serializer.data)


class Category1View(viewsets.ModelViewSet):
    pass
