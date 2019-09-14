# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20190912_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='chinese_movie_name',
            field=models.CharField(max_length=250, verbose_name='\u4e2d\u6587\u7535\u5f71\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='dyttdetail',
            field=models.CharField(max_length=256, null=True, verbose_name='\u7535\u5f71\u5929\u5802\u8be6\u60c5\u5730\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to=b'movie/', null=True, verbose_name='\u7535\u5f71\u6d77\u62a5', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_detail_pic',
            field=models.ImageField(upload_to=b'movie/', null=True, verbose_name='\u7535\u5f71\u8be6\u60c5\u9875\u5267\u60c5\u56fe', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_head_pic',
            field=models.ImageField(upload_to=b'movie/', null=True, verbose_name='\u7535\u5f71\u8be6\u60c5\u9875\u5934\u56fe', blank=True),
        ),
    ]
