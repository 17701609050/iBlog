# Generated by Django 2.1.7 on 2019-10-17 15:13

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20190913_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='aboutmovie',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='关于电影'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movie/', verbose_name='电影海报'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_detail_pic',
            field=models.ImageField(blank=True, null=True, upload_to='movie/', verbose_name='电影详情页剧情图'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_head_pic',
            field=models.ImageField(blank=True, null=True, upload_to='movie/', verbose_name='电影详情页头图'),
        ),
    ]
