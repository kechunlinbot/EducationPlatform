# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-10 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class', verbose_name='班级')),
            ],
            options={
                'verbose_name': '班级老师',
                'verbose_name_plural': '班级老师',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=20, unique=True, verbose_name='英文名')),
                ('passwd', models.CharField(max_length=200, verbose_name='密码')),
                ('real_name', models.CharField(max_length=20, verbose_name='真实姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('degree', models.CharField(choices=[('undergraduate', '专科/本科'), ('master', '硕士研究生'), ('doctor', '博士研究生')], default='undergraduate', max_length=13, verbose_name='学历')),
                ('major', models.CharField(max_length=30, verbose_name='专业')),
                ('school', models.CharField(max_length=20, verbose_name='学校')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '教师管理',
                'verbose_name_plural': '教师管理',
            },
        ),
        migrations.AddField(
            model_name='classteacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher', verbose_name='教师'),
        ),
    ]
