from django.db import models
from datetime import datetime

from classes.models import Class


# class HomeWork(models.Model):
#     name = models.CharField(max_length=30, unique=True, verbose_name='题目名')
#     content = models.TextField(verbose_name='内容')
#     class_work = models.ForeignKey(Class, verbose_name='班级')
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = '作业管理'
#         verbose_name_plural = verbose_name
#
#     def __repr__(self):
#         return self.name
