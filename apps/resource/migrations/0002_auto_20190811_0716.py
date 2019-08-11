# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='extraction_code',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='resource',
            name='add_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(unique=True, max_length=250, verbose_name='\u8d44\u6e90\u540d\u79f0', db_index=True),
        ),
    ]
