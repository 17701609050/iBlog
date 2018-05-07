# -*- coding: UTF-8 -*-
from apps.rest.base.mixins import *
from apps.rest.blog.serializers import *


class BlogView(MultipleFieldLookupMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):

    def get_serializer_class(self):
        return BlogViewSerializer
