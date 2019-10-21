# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('head_pic_url', models.CharField(default=b'/static/admin/img/icon_addlink.gif', max_length=250, null=True, verbose_name='\u5934\u56fe\u94fe\u63a5', blank=True)),
                ('phone_number', models.CharField(max_length=20, verbose_name='\u624b\u673a\u53f7', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u4e2a\u4eba\u7b80\u4ecb',
                'verbose_name_plural': '\u4e2a\u4eba\u7b80\u4ecb',
            },
        ),
        migrations.CreateModel(
            name='ProfileTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
                'verbose_name': '\u4e2a\u4eba\u7b80\u4ecb\u6807\u7b7e',
                'verbose_name_plural': '\u4e2a\u4eba\u7b80\u4ecb\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(to='user.ProfileTag', verbose_name='\u6807\u7b7e', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
