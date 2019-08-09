# -*- coding: UTF-8 -*-
import xadmin
from django.db.models import TextField
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings
from .models import ResourceCategory, Resource


class ResourceCategoryAdmin(object):
    list_display = ('resource_category', 'display_name')


class ResourceAdmin(object):
    list_display = ('name', 'category', 'tag', 'link')


xadmin.site.register(ResourceCategory, ResourceCategoryAdmin)
xadmin.site.register(Resource, ResourceAdmin)


#Register your models here.
