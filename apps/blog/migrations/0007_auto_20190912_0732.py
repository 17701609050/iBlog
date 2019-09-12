# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190912_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='head_pic_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(default=b'favicon.ico', null=True, upload_to=b'img/', blank=True),
        ),
    ]
