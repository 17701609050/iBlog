# -*- coding: UTF-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from apps.rest.base.mixins import *
from apps.rest.blog.serializers import *
# from apps.blog.models import Blog, Category2


class BlogViewSets(MultipleFieldLookupMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('id', 'title', 'pub_time', 'brief', 'content', 'page_views')
    search_fields = ('id', 'title', 'brief', 'content', 'page_views', 'category2__display_name',
                     'category1__display_name')
    ordering = ('-pub_time',)

    def get_serializer_class(self):
            return BlogViewSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            serializer_data = serializer.data
            for serializer in serializer_data:
                category2 = Category2.objects.get(id=serializer["category2"])
                serializer.update({"category2_name": category2.display_name})
            return self.get_paginated_response(serializer_data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def get_blogs(self, request, *args, **kwargs):
        blog_all = Blog.objects.all()
        page = self.paginate_queryset(blog_all)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(blog_all, many=True)
        return Response(serializer.data)


class Category1ViewSets(viewsets.ModelViewSet):

    queryset = Category1.objects.all()
    serializer_class = Category1ViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class Category2ViewSets(viewsets.ModelViewSet):
    queryset = Category2.objects.all()
    serializer_class = Category2ViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class TagViewSets(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class ProfileTagViewSets(viewsets.ModelViewSet):
    queryset = Profile_Tag.objects.all()
    serializer_class = ProfileTagViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class ProfileViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class FriendTagViewSets(viewsets.ModelViewSet):
    queryset = Friend_Tag.objects.all()
    serializer_class = FriendTagViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class FriendViewSets(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendViewSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
