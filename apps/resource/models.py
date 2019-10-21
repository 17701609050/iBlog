# -*- coding:utf8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from apps.blog.models import Tag


class ResourceCategory(models.Model):
    resource_category = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.resource_category

    def __str__(self):
        return "%s" % (self.resource_category)

    class Meta:
        verbose_name = '资源分类'
        verbose_name_plural = '资源分类'
        ordering = ['-add_time']


class ResourceTag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    def __str__(self):
        return "%s" % (self.tag)

    class Meta:
        verbose_name = '资源标签'
        verbose_name_plural = '资源标签'
        ordering = ['-add_time']


class Resource(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, verbose_name=u'资源名称')
    category = models.ForeignKey(ResourceCategory, verbose_name=u'资源分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(ResourceTag, blank=True, verbose_name=u'标签')
    link = models.CharField(max_length=255)
    add_time = models.DateTimeField()
    extraction_code = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = '资源'
        ordering = ['-add_time']









