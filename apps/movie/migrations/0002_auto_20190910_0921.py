# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': '\u7535\u5f71', 'verbose_name_plural': '\u7535\u5f71'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='aboutmovie',
            field=DjangoUeditor.models.UEditorField(default=b'', verbose_name='\u5173\u4e8e\u7535\u5f71'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.CharField(max_length=256, null=True, verbose_name='\u4e3b\u6f14', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=64, null=True, verbose_name='\u4e0a\u6620\u56fd\u5bb6', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='dateyear',
            field=models.CharField(max_length=64, null=True, verbose_name='\u4e0a\u6620\u65e5\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=256, null=True, verbose_name='\u5bfc\u6f14', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='doubanlink',
            field=models.CharField(max_length=256, null=True, verbose_name='\u8c46\u74e3\u94fe\u63a5', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='doubanscore',
            field=models.CharField(max_length=64, null=True, verbose_name='\u8c46\u74e3\u8bc4\u5206', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='downloadlink',
            field=models.CharField(max_length=256, null=True, verbose_name='\u7535\u5f71\u4e0b\u8f7d\u94fe\u63a5', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to=b'movie/', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbscore',
            field=models.CharField(max_length=64, null=True, verbose_name='IMDB\u8bc4\u5206', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=64, null=True, verbose_name='\u7535\u5f71\u8bed\u8a00', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='moviename',
            field=models.CharField(max_length=64, verbose_name='\u7535\u5f71\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='spidertime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u7535\u5f71\u5165\u5e93\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='style',
            field=models.CharField(max_length=64, null=True, verbose_name='\u7535\u5f71\u7c7b\u578b', blank=True),
        ),
    ]
