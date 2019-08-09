# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as resource_view

urlpatterns = [
   url(r'', resource_view.resource_index, name='blog_index'),

]
