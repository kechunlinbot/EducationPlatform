# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-02 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='英文名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('real_name', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('degree', models.CharField(choices=[('high school', '中专/高中'), ('undergraduate', '专科/本科'), ('master', '硕士研究生'), ('doctor', '博士研究生')], default='undergraduate', max_length=20, verbose_name='学历')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('height', models.IntegerField(verbose_name='身高')),
                ('weight', models.IntegerField(verbose_name='体重')),
                ('learning', models.TextField(verbose_name='学习经历')),
                ('allergies', models.TextField(verbose_name='过敏史')),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='注册时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('class_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.ClassModel', verbose_name='所属班级')),
            ],
            options={
                'verbose_name': '学生管理',
                'verbose_name_plural': '学生管理',
            },
        ),
    ]
