# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-29 21:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('teachers', '0002_auto_20171229_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='英文名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('real_name', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('degree', models.CharField(choices=[('undergraduate', '专科/本科'), ('master', '硕士研究生'), ('doctor', '博士研究生')], default='undergraduate', max_length=20, verbose_name='学历')),
                ('major', models.CharField(max_length=50, verbose_name='专业')),
                ('school', models.CharField(max_length=50, verbose_name='学校')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='注册时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.ClassModel', verbose_name='所属班级')),
            ],
            options={
                'verbose_name_plural': '教师管理',
                'verbose_name': '教师管理',
            },
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]