# @author shi.qi.chang
from django.db import models
from django.utils import timezone

from classes.models import Class

GENDERS = (
    ('male', '男'),
    ('female', '女'),
)

DEGREES = (
    ('undergraduate', '专科/本科'),
    ('master', '硕士研究生'),
    ('doctor', '博士研究生'),
)


class Teacher(models.Model):
    en_name = models.CharField(max_length=20, unique=True, verbose_name='英文名')
    password = models.CharField(max_length=50, verbose_name='密码')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='性别', default='male')
    degree = models.CharField(max_length=13, choices=DEGREES, verbose_name='学历', default='undergraduate')
    major = models.CharField(max_length=30, verbose_name='专业')
    school = models.CharField(max_length=20, verbose_name='学校')
    email = models.EmailField(verbose_name='邮箱')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师管理'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.en_name


class ClassTeacher(models.Model):
    class_name = models.ForeignKey(Class, verbose_name='班级')
    teacher = models.ForeignKey(Teacher, verbose_name='教师')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '班级老师'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '%s:%s' % (self.class_name, self.teacher)
