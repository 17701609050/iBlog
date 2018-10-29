# -*- coding:utf-8 -*-

from apps.blog.models import Blog, Category1, Category2, Tag, Profile_Tag, Profile, Friend_Tag, Friend
from apps.rest.base.viewsets import *


class BlogViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class Category1ViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = '__all__'


class Category2ViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category2
        fields = '__all__'


class TagViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ProfileTagViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile_Tag
        fields = '__all__'


class ProfileViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class FriendTagViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend_Tag
        fields = '__all__'


class FriendViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = '__all__'
