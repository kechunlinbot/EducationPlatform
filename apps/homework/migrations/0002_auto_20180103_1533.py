# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-03 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkmodel',
            name='class_work',
        ),
        migrations.DeleteModel(
            name='HomeWorkModel',
        ),
    ]
