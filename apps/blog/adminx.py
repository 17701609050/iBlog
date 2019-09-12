# -*- coding: UTF-8 -*-
import xadmin
from django.db.models import TextField
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings
from .models import Blog, Category1, Category2, Tag, Profile, Profile_Tag, Friend, Friend_Tag


class XadminUEditorWidget(UEditorWidget):
    def __init__(self,**kwargs):
        self.ueditor_options=kwargs
        self.Media.js = None
        super(XadminUEditorWidget, self).__init__(kwargs)


class UeditorPlugin(BaseAdminPlugin):

    def get_field_style(self, attrs, db_field, style, **kwargs):
        if style == 'ueditor':
            if isinstance(db_field, UEditorField):
                widget = db_field.formfield().widget
                param = {}
                param.update(widget.ueditor_settings)
                param.update(widget.attrs)
                return {'widget': XadminUEditorWidget(**param)}
            if isinstance(db_field, TextField):
                return {'widget': XadminUEditorWidget}
        return attrs

    def block_extrahead(self, context, nodes):
        js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/ueditor/ueditor.config.js")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/ueditor/ueditor.all.min.js")
        nodes.append(js)


class BlogAdmin(object):
    list_display = ('title', 'pub_time', 'category1', 'category2', 'page_views')
    search_field = ('category1', 'category2')
    list_filter = ('category1', 'category2')
    style_fields = {'content': 'ueditor'}


class Category1Admin(object):
    list_display = ('category_1', 'display_name')


class Category2Admin(object):
    list_display = ('category_2', 'category1', 'display_name')


class ProfileAdmin(object):
    list_display = ('title', 'pub_time')
    style_fields = {'content': 'ueditor'}


class FriendAdmin(object):
    list_display = ('name', 'friend_url')


xadmin.site.register_plugin(UeditorPlugin, DetailAdminView)
xadmin.site.register_plugin(UeditorPlugin, ModelFormAdminView)

xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Category1, Category1Admin)
xadmin.site.register(Category2, Category2Admin)
xadmin.site.register(Tag)
xadmin.site.register(Profile, ProfileAdmin)
xadmin.site.register(Profile_Tag)
xadmin.site.register(Friend, FriendAdmin)
xadmin.site.register(Friend_Tag)

# Register your models here.
