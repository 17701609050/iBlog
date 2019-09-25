# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190912_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_from',
            field=models.CharField(default=b'', max_length=50, verbose_name='\u7528\u6237\u6765\u6e90', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u81ea\u6211\u63cf\u8ff0'),
        ),
    ]
