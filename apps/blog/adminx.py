# -*- coding: UTF-8 -*-
import xadmin
from django.db.models import TextField
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings
from xadmin.views import CommAdminView
from .models import Blog, Category1, Category2, Tag, Profile, Profile_Tag, Friend, Friend_Tag


class CustomView(object):
    site_title = 'TimeBack博客后台管理'  # 网页头部导航
    site_footer = '2019 · 鄂ICP备19022350号 · Powered by 阿里云'  # 底部版权内容
    menu_style = 'accordion'  # 左侧导航折叠框


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

    # Media,添加到footer中的js文件
    def get_media(self, media):
        media = media + self.vendor('xadmin.widget.select.js', 'xadmin.widget.select-transfer.js',
                                    'xadmin.plugin.quick-form.js', 'xadmin.widget.datetime.js')
        return media

    def block_extrahead(self, context, nodes):
        js = ''
        # 解决ueditor插件跟select2冲突
        js += '<link href="%s" type="text/css" media="screen" rel="stylesheet" />' % (settings.STATIC_URL + "/xadmin/vendor/select2/select2.css" )
        js += '<link href="%s" type="text/css" media="screen" rel="stylesheet" />' % (settings.STATIC_URL + "/xadmin/vendor/selectize/selectize.css" )
        js += '<link href="%s" type="text/css" media="screen" rel="stylesheet" />' % (settings.STATIC_URL + "/xadmin/vendor/selectize/selectize.bootstrap3.css" )
        js += '<link href="%s" type="text/css" media="screen" rel="stylesheet" />' % (settings.STATIC_URL + "/xadmin/vendor/select2/select2.css" )
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/xadmin/vendor/selectize/selectize.js")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/xadmin/vendor/select2/select2.js")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/xadmin/vendor/select2/select2_locale_zh-hans.js")

        # 解决ueditor插件跟bootstrap-datepicker冲突
        js += '<link href="%s" type="text/css" media="screen" rel="stylesheet" />' % (settings.STATIC_URL + "/xadmin/vendor/bootstrap-datepicker/css/datepicker.css")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/xadmin/vendor/bootstrap-datepicker/js/bootstrap-datepicker.js")
        js += '<link href="%s" type="text/css" media="screen" rel="stylesheet" />' % (settings.STATIC_URL + "/xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.css")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.js")

        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/ueditor/ueditor.config.js")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "/ueditor/ueditor.all.min.js")
        nodes.append(js)


class BlogAdmin(object):
    list_display = ('title', 'pub_time', 'category1', 'category2', 'page_views')
    search_field = ('category1', 'category2')
    list_filter = ('category1', 'category2')
    style_fields = {'content': 'ueditor'}
    list_editable = ['title', 'pub_time', 'category1', 'category2']


class Category1Admin(object):
    list_display = ('category_1', 'display_name')


class Category2Admin(object):
    list_display = ('category_2', 'category1', 'display_name')


class ProfileAdmin(object):
    list_display = ('title', 'pub_time')
    style_fields = {'content': 'ueditor'}


class FriendAdmin(object):
    list_display = ('name', 'friend_url')


xadmin.site.register(CommAdminView, CustomView)

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
