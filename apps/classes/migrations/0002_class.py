# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-03 15:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=30, unique=True, verbose_name='班级名称')),
                ('class_major', models.CharField(max_length=20, verbose_name='班级专业')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '班级管理',
                'verbose_name_plural': '班级管理',
                'db_table': 'classes',
            },
        ),
    ]