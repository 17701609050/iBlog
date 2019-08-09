# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190719_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250, db_index=True)),
                ('link', models.CharField(max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
                'verbose_name': '\u8d44\u6e90',
                'verbose_name_plural': '\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='ResourceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_category', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('display_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-add_time'],
                'verbose_name': '\u8d44\u6e90\u5206\u7c7b',
                'verbose_name_plural': '\u8d44\u6e90\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(verbose_name='\u8d44\u6e90\u5206\u7c7b', to='resource.ResourceCategory'),
        ),
        migrations.AddField(
            model_name='resource',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
