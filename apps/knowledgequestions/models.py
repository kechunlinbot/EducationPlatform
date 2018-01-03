# @author shi.qi.chang
from django.db import models
from datetime import datetime

DIFFICULTY_LEVELS = (
    ('beginner', '初级'),
    ('intermediate', '中级'),
    ('advanced', '高级'),
)


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='课程名字')
    detail = models.TextField(verbose_name='课程详情')
    difficulty_level = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS, default='beginner', verbose_name='难易程度')
    category = models.CharField(max_length=20, default='后端', verbose_name='课程类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        db_table = 'courses'

    def __repr__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=20, verbose_name='模块名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '知识模块'
        verbose_name_plural = verbose_name
        db_table = 'modules'

    def __repr__(self):
        return self.name

    def get_knowledgebase(self):
        return self.knowledgebase_set.all()


class KnowledgeBase(models.Model):
    module = models.ForeignKey(Module, verbose_name='知识模块')
    name = models.CharField(max_length=50, verbose_name='二级模块')
    knowledge_point = models.CharField(max_length=100, null=True, blank=True, verbose_name='知识点')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '知识库'
        verbose_name_plural = verbose_name
        db_table = 'knowledgebase'

    def __repr__(self):
        return self.name


class QuestionBank(models.Model):
    title = models.CharField(max_length=50, verbose_name='题目名称')
    content = models.TextField(verbose_name='题目内容')
    difficulty_level = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS, default='beginner', verbose_name='难易程度')
    knowledge_module = models.ForeignKey(Module, verbose_name='知识模块')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '题库'
        verbose_name_plural = verbose_name
        db_table = 'questionbank'

    def __repr__(self):
        return self.title