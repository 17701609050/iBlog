# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_auto_20190811_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
                'verbose_name': '\u8d44\u6e90\u6807\u7b7e',
                'verbose_name_plural': '\u8d44\u6e90\u6807\u7b7e',
            },
        ),
        migrations.AlterField(
            model_name='resource',
            name='tag',
            field=models.ManyToManyField(to='resource.ResourceTag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
