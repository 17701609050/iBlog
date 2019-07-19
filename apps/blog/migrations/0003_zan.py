# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181015_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zan_num', models.IntegerField(default=0)),
            ],
        ),
    ]
