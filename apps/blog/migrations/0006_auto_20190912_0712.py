# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-pub_time'], 'verbose_name': '\u4f5c\u8005\u4e2a\u4eba\u7b80\u4ecb', 'verbose_name_plural': '\u4f5c\u8005\u4e2a\u4eba\u7b80\u4ecb'},
        ),
    ]
