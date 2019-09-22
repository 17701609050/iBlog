# -*- coding:utf8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
# django-ckeditor
from ckeditor.fields import RichTextField
# django-mptt
from mptt.models import MPTTModel, TreeForeignKey


class Category1(models.Model):
    category_1 = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.category_1

    class Meta:
        verbose_name = '一级分类'
        verbose_name_plural = '一级分类'
        ordering = ['-add_time']


class Category2(models.Model):
    category_2 = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=255)
    category1 = models.ForeignKey(Category1, verbose_name=u'一级目录')

    def __unicode__(self):
        return self.category_2

    class Meta:
        verbose_name = '二级分类'
        verbose_name_plural = '二级分类'
        ordering = ['-add_time']


class Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['-add_time']


class Blog(models.Model):
    title = models.CharField(u'标题', max_length=100)
    head_pic_url = models.ImageField(u'文章标题链接', upload_to="blog/", blank=True, null=True)
    pub_time = models.DateTimeField(u'发布时间')
    brief = models.CharField(u'摘要', max_length=200, blank=True, null=True)
    content = UEditorField(u'正文', width="100%", height=600, toolbars="full", imagePath="blog/", settings={})
    page_views = models.PositiveIntegerField(u'阅读量', default=0, editable=False)
    category1 = models.ForeignKey(Category1, verbose_name=u'一级目录')
    category2 = models.ForeignKey(Category2, null=True, verbose_name=u'二级目录')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
        ordering = ['-pub_time']


class Profile_Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = '个人简介标签'
        verbose_name_plural = '个人简介标签'
        ordering = ['-add_time']


class Profile(models.Model):
    title = models.CharField(u'标题', max_length=100)
    user_image = models.ImageField(upload_to="img/", blank=True, null=True, default='favicon.ico')
    # head_pic_url = models.CharField(u'头图链接', max_length=250, default='/static/img/default.jpg', null=True, blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    content = UEditorField(u'正文', width='100%', height=600, toolbars="full", imagePath="", settings={})
    tags = models.ManyToManyField(Profile_Tag, blank=True, verbose_name=u'标签')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '作者个人简介'
        verbose_name_plural = '作者个人简介'
        ordering = ['-pub_time']


class Friend_Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = '友情链接标签'
        verbose_name_plural = '友情链接标签'
        ordering = ['-add_time']


class Friend(models.Model):
    name = models.CharField(u'友情链接网站名称',max_length=50, db_index=True, unique=True)
    friend_url = models.CharField(u'链接', max_length=250, default='http://')
    tags = models.ManyToManyField(Friend_Tag, blank=True, verbose_name=u'标签')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
        ordering = ['name']


class Zan(models.Model):
    ip_address = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.ip_address


class Comment(MPTTModel):
    article = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    # mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    # 记录二级评论回复给谁, str
    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]

