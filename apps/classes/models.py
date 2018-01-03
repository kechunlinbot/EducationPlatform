from django.db import models
from datetime import datetime


# Create your models here.

class ClassModel(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='班级名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '班级管理'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.class_name
