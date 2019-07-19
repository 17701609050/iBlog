# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pub_time'], 'verbose_name': '\u535a\u5ba2', 'verbose_name_plural': '\u535a\u5ba2'},
        ),
        migrations.AlterModelOptions(
            name='category1',
            options={'ordering': ['-add_time'], 'verbose_name': '\u4e00\u7ea7\u5206\u7c7b', 'verbose_name_plural': '\u4e00\u7ea7\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='category2',
            options={'ordering': ['-add_time'], 'verbose_name': '\u4e8c\u7ea7\u5206\u7c7b', 'verbose_name_plural': '\u4e8c\u7ea7\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='friend',
            options={'ordering': ['name'], 'verbose_name': '\u53cb\u60c5\u94fe\u63a5', 'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5'},
        ),
        migrations.AlterModelOptions(
            name='friend_tag',
            options={'ordering': ['-add_time'], 'verbose_name': '\u53cb\u60c5\u94fe\u63a5\u6807\u7b7e', 'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5\u6807\u7b7e'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-pub_time'], 'verbose_name': '\u4e2a\u4eba\u7b80\u4ecb', 'verbose_name_plural': '\u4e2a\u4eba\u7b80\u4ecb'},
        ),
        migrations.AlterModelOptions(
            name='profile_tag',
            options={'ordering': ['-add_time'], 'verbose_name': '\u4e2a\u4eba\u7b80\u4ecb\u6807\u7b7e', 'verbose_name_plural': '\u4e2a\u4eba\u7b80\u4ecb\u6807\u7b7e'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-add_time'], 'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_time',
            field=models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
