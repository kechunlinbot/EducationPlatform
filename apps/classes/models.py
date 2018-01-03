# @author shi.qi.chang
from django.db import models
from datetime import datetime


class Class(models.Model):
    class_name = models.CharField(max_length=30, unique=True, verbose_name='班级名称')
    class_major = models.CharField(max_length=20, verbose_name='班级专业')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '班级管理'
        verbose_name_plural = verbose_name
        db_table = 'classes'

    def __repr__(self):
        return self.class_name
