# -*- coding:utf8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User


class ProfileTag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = '个人简介标签'
        verbose_name_plural = '个人简介标签'
        ordering = ['-add_time']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(u'标题', max_length=100)
    head_pic_url = models.CharField(u'头图链接', max_length=250, default='/static/admin/img/icon_addlink.gif',
                                    null=True, blank=True)
    phone_number = models.CharField(u'手机号', max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    content = UEditorField(u'正文', width=900, height=600, toolbars="full", imagePath="", settings={})
    tags = models.ManyToManyField('ProfileTag', blank=True, verbose_name=u'标签')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '个人简介'
        verbose_name_plural = '个人简介'
        ordering = ['-create_time']








