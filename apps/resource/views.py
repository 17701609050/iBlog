# -*- coding: UTF-8 -*-
# Create your views here.

# some function would be used in views
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.resource.models import Resource


def resource_index(request):
    resources = Resource.objects.all()
    content = {
        'resources': resources
    }
    return render(request, 'resource/resource.html', content)
