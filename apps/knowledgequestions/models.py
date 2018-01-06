# @author shi.qi.chang
from django.db import models
from django.contrib.auth.models import User

DIFFICULTY_LEVELS = (
    ('beginner', '初级'),
    ('intermediate', '中级'),
    ('advanced', '高级'),
)


class Course(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='课程名字')
    detail = models.CharField(max_length=100, verbose_name='课程详情')
    difficulty_level = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS, default='beginner', verbose_name='难易程度')
    category = models.CharField(max_length=20, default='后端', verbose_name='课程类型')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    creater = models.ForeignKey(User, default='', related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', blank=True, verbose_name='修改者')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=20, verbose_name='模块名称')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    creater = models.ForeignKey(User, default='', related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', blank=True, verbose_name='修改者')

    class Meta:
        verbose_name = '知识模块'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name

    def get_knowledgebase(self):
        return self.knowledgebase_set.all()


class KnowledgeBase(models.Model):
    module = models.ForeignKey(Module, verbose_name='知识模块')
    name = models.CharField(max_length=30, verbose_name='二级模块')
    knowledge_point = models.CharField(max_length=50, blank=True, verbose_name='知识点')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    creater = models.ForeignKey(User, default='', related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', blank=True, verbose_name='修改者')

    class Meta:
        verbose_name = '知识库'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name


class QuestionBank(models.Model):
    title = models.CharField(max_length=20, verbose_name='题目名称')
    content = models.CharField(max_length=500, verbose_name='题目内容')
    difficulty_level = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS, default='beginner', verbose_name='难易程度')
    module = models.ForeignKey(Module, verbose_name='知识模块')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    creater = models.ForeignKey(User, default='', related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', blank=True, verbose_name='修改者')

    class Meta:
        verbose_name = '题库'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.title
