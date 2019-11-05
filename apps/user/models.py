# -*- coding:utf8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User


class ProfileTag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    def __str__(self):
        return "%s" % (self.tag)

    class Meta:
        verbose_name = '个人简介标签'
        verbose_name_plural = '个人简介标签'
        ordering = ['-add_time']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(u'标题', max_length=100)
    user_image = models.ImageField(u'用户头像', upload_to="img/", blank=True, null=True, max_length=250, default='favicon.ico')  # 表示图片保存地址
    # head_pic_url = models.CharField(u'头图链接', max_length=250, default='/static/img/favicon.ico',
    #                                 null=True, blank=True)
    phone_number = models.CharField(u'手机号', max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    content = UEditorField(u'自我描述', width=900, height=600, toolbars="full", imagePath="user/", settings={})
    tags = models.ManyToManyField('ProfileTag', blank=True, verbose_name=u'标签')
    uid = models.CharField(u'用户唯一ID', max_length=50, default='', null=False, blank=True)
    user_from = models.CharField(u'用户来源', max_length=50, default='', null=False, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name = '个人简介'
        verbose_name_plural = '个人简介'
        ordering = ['-create_time']








