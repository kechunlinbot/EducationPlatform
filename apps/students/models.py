from django.db import models
from datetime import datetime

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


class Students(models.Model):
    """学生类"""

    name = models.CharField(max_length=50, unique=True, verbose_name='英文名')
    password = models.CharField(max_length=200, verbose_name='密码')
    real_name = models.CharField(max_length=50, verbose_name='真实姓名')
    gender = models.CharField(max_length=1, choices=GENDERS, verbose_name='性别')
    degree = models.CharField(max_length=1, choices=DEGREES, verbose_name='学历')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    height = models.IntegerField(verbose_name='身高')
    weight = models.IntegerField(verbose_name='体重')
    learning = models.TextField(verbose_name='学习经历')
    allergies = models.TextField(verbose_name='过敏史')
    reg_date = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name