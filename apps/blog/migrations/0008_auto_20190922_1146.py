# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190912_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='head_pic_url',
            field=models.ImageField(upload_to=b'blog/', null=True, verbose_name='\u6587\u7ae0\u6807\u9898\u94fe\u63a5', blank=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='\u53cb\u60c5\u94fe\u63a5\u7f51\u7ad9\u540d\u79f0', db_index=True),
        ),
    ]
