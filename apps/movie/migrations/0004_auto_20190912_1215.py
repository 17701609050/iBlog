# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20190910_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_detail_pic',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_head_pic',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='downloadlink',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u7535\u5f71\u4e0b\u8f7d\u94fe\u63a5', blank=True),
        ),
    ]
