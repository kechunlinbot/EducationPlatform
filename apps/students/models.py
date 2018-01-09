# @author shi.qi.chang
from django.db import models
from django.utils import timezone

from classes.models import Class

GENDERS = (
    ('male', '男'),
    ('female', '女'),
)

DEGREES = (
    ('high school', '中专/高中'),
    ('undergraduate', '专科/本科'),
    ('master', '硕士研究生'),
    ('doctor', '博士研究生'),
)


class Student(models.Model):
    en_name = models.CharField(max_length=20, unique=True, verbose_name='英文名')
    passwd = models.CharField(max_length=50, verbose_name='密码')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='性别', default='male')
    degree = models.CharField(max_length=13, choices=DEGREES, verbose_name='学历', default='undergraduate')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    height = models.IntegerField(verbose_name='身高')
    weight = models.IntegerField(verbose_name='体重')
    learning = models.CharField(max_length=200, verbose_name='学习经历')
    allergies = models.CharField(max_length=200, verbose_name='过敏史')
    class_name = models.ForeignKey(Class, verbose_name='所属班级')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '学生管理'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.en_name

    __str__ = __repr__
