# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-10 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgequestions', '0002_auto_20180110_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='difficulty_level',
            field=models.CharField(choices=[('beginner', '初级'), ('intermediate', '中级'), ('advanced', '高级')], default='beginner', max_length=10, verbose_name='难易程度'),
        ),
    ]
