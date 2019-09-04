# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.CharField(default=b'', max_length=50, verbose_name='\u7528\u6237\u552f\u4e00ID', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='head_pic_url',
            field=models.CharField(default=b'/static/img/favicon.ico', max_length=250, null=True, verbose_name='\u5934\u56fe\u94fe\u63a5', blank=True),
        ),
    ]
