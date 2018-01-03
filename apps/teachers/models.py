# @author shi.qi.chang
from django.db import models
from datetime import datetime

<<<<<<< Updated upstream
from classes.models import ClassModel
=======
from classes.models import Class
>>>>>>> Stashed changes

GENDERS = (
    ('male', '男'),
    ('female', '女'),
)

DEGREES = (
    ('undergraduate', '专科/本科'),
    ('master', '硕士研究生'),
    ('doctor', '博士研究生'),
)


<<<<<<< Updated upstream
class TeachersModel(models.Model):
    """教师类"""

=======
class Teacher(models.Model):
>>>>>>> Stashed changes
    name = models.CharField(max_length=50, unique=True, verbose_name='英文名')
    password = models.CharField(max_length=200, verbose_name='密码')
    real_name = models.CharField(max_length=50, verbose_name='真实姓名')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='性别', default='male')
    degree = models.CharField(max_length=20, choices=DEGREES, verbose_name='学历', default='undergraduate')
    major = models.CharField(max_length=50, verbose_name='专业')
    school = models.CharField(max_length=50, verbose_name='学校')
    email = models.EmailField(verbose_name='邮箱')
<<<<<<< Updated upstream
    reg_date = models.DateTimeField(default=datetime.now, verbose_name='注册时间')
    class_teacher = models.ForeignKey(ClassModel, verbose_name='所属班级')
=======
>>>>>>> Stashed changes
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师管理'
        verbose_name_plural = verbose_name
        db_table = 'teachers'

    def __repr__(self):
        return self.name


class ClassTeacher(models.Model):
    class_name = models.ForeignKey(Class, verbose_name='班级')
    teacher = models.ForeignKey(Teacher, verbose_name='教师')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '班级老师'
        verbose_name_plural = verbose_name
        db_table = 'classes_teachers'

    def __repr__(self):
        return '%s:%s' % (self.class_name, self.teacher)