# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_zan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zan',
            name='zan_num',
        ),
        migrations.AddField(
            model_name='zan',
            name='ip_address',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
