# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('head_pic_url', models.CharField(default=b'/static/img/zipinglx.png', max_length=250, verbose_name='\u5934\u56fe\u94fe\u63a5')),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('brief', models.CharField(max_length=200, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='\u6b63\u6587')),
                ('page_views', models.PositiveIntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf', editable=False)),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_1', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('display_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_2', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('display_name', models.CharField(max_length=255)),
                ('category1', models.ForeignKey(verbose_name='\u4e00\u7ea7\u76ee\u5f55', to='blog.Category1')),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, db_index=True)),
                ('friend_url', models.CharField(default=b'http://', max_length=250, verbose_name='\u94fe\u63a5')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Friend_Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('head_pic_url', models.CharField(default=b'/static/img/default.jpg', max_length=250, null=True, verbose_name='\u5934\u56fe\u94fe\u63a5', blank=True)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Profile_Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(to='blog.Profile_Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
        migrations.AddField(
            model_name='friend',
            name='tags',
            field=models.ManyToManyField(to='blog.Friend_Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='category1',
            field=models.ForeignKey(verbose_name='\u4e00\u7ea7\u76ee\u5f55', to='blog.Category1'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category2',
            field=models.ForeignKey(verbose_name='\u4e8c\u7ea7\u76ee\u5f55', to='blog.Category2', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
