# -*- coding: UTF-8 -*-
import xadmin
from django.db.models import TextField
from DjangoUeditor.models import UEditorField
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings
from django.contrib.auth.models import User
from .models import Movie, MovieComent


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


class MovieAdmin(object):
    list_display = ('moviename', 'doubanlink', 'doubanscore', 'imdbscore', 'director', 'actor', 'country', 'style',
                    'dateyear', 'downloadlink', 'spidertime', 'aboutmovie')
    style_fields = {'aboutmovie': 'ueditor'}


xadmin.site.register_plugin(UeditorPlugin, DetailAdminView)
xadmin.site.register_plugin(UeditorPlugin, ModelFormAdminView)
xadmin.site.register(Movie, MovieAdmin)

