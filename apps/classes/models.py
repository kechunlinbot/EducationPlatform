# @author shi.qi.chang
from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='班级名称')
    major = models.CharField(max_length=20, verbose_name='班级专业')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    administrator = models.ForeignKey(User, default='', related_name='+', verbose_name='管理员')

    class Meta:
        verbose_name = '班级管理'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name
