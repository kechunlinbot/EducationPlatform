from django.db import models

GENDERS = (
    ('1', '男'),
    ('2', '女'),
)

DEGREES = (
    ('1', '小学'),
    ('2', '初中'),
    ('3', '中专/高中'),
    ('4', '专科/本科'),
    ('5', '硕士研究生'),
    ('6', '博士研究生'),
)

STATUS = (
    ('1', '学习期内'),
    ('2', '毕业'),
)


class Persons(models.Model):
    """学生类和教师类的抽象基类"""

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, verbose_name='英文名')
    password = models.CharField(max_length=200, verbose_name='，密码')
    real_name = models.CharField(max_length=50, verbose_name='真实姓名')
    gender = models.CharField(max_length=1, choices=GENDERS, verbose_name='性别')
    degree = models.CharField(max_length=1, choices=DEGREES, verbose_name='学历')
    reg_date = models.DateTimeField(verbose_name='注册时间')

    class Meta:
        abstract = True  # 定义本类为抽象基类


class Students(Persons):
    """学生类"""

    # stu_class = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='所在班级')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    height = models.IntegerField(verbose_name='身高')
    weight = models.IntegerField(verbose_name='体重')
    learning = models.TextField(verbose_name='学习经历')
    allergies = models.TextField(verbose_name='过敏史')
    status = models.CharField(max_length=1, choices=STATUS, null=True)


class Teachers(Persons):
    """教师类"""

    # tch_class = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='授课班级')
    major = models.CharField(max_length=50, verbose_name='专业')
    school = models.CharField(max_length=50, verbose_name='学校')
    email = models.EmailField(verbose_name='邮箱')
