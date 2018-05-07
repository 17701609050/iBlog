# -*- coding:utf-8 -*-

from apps.blog.models import Blog
from apps.rest.base.viewsets import *

class BlogViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'