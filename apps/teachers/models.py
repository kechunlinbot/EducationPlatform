from django.db import models
from datetime import datetime

GENDERS = (
    ('male', '男'),
    ('female', '女'),
)

DEGREES = (
    ('undergraduate', '专科/本科'),
    ('master', '硕士研究生'),
    ('doctor', '博士研究生'),
)


class Teachers(models.Model):
    """教师类"""

    name = models.CharField(max_length=50, unique=True, verbose_name='英文名')
    password = models.CharField(max_length=200, verbose_name='密码')
    real_name = models.CharField(max_length=50, verbose_name='真实姓名')
    gender = models.CharField(max_length=1, choices=GENDERS, verbose_name='性别')
    degree = models.CharField(max_length=1, choices=DEGREES, verbose_name='学历')
    major = models.CharField(max_length=50, verbose_name='专业')
    school = models.CharField(max_length=50, verbose_name='学校')
    email = models.EmailField(verbose_name='邮箱')
    reg_date = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name
