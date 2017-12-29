# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-29 19:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='英文名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('real_name', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('gender', models.CharField(choices=[('1', '男'), ('2', '女')], max_length=1, verbose_name='性别')),
                ('degree', models.CharField(choices=[('4', '专科/本科'), ('5', '硕士研究生'), ('6', '博士研究生')], max_length=1, verbose_name='学历')),
                ('major', models.CharField(max_length=50, verbose_name='专业')),
                ('school', models.CharField(max_length=50, verbose_name='学校')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='注册时间')),
            ],
        ),
    ]
