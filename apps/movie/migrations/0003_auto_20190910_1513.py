# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20190910_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='counter',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_length',
            field=models.CharField(max_length=50, null=True, verbose_name='\u7535\u5f71\u65f6\u957f', blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='translation_name',
            field=models.CharField(max_length=250, verbose_name='\u7535\u5f71\u8bd1\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='moviename',
            field=models.CharField(max_length=250, verbose_name='\u7535\u5f71\u540d\u79f0', blank=True),
        ),
    ]
