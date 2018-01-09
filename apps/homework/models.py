# @author shi.qi.chang
from django.db import models
from django.utils import timezone

from classes.models import Class
from teachers.models import Teacher
from knowledgequestions.models import QuestionBank

IS_BONUS = (
    ('1', '是'),
    ('0', '否'),
)

IS_COMPLETE = IS_BONUS


class Assignment(models.Model):
    question = models.ForeignKey(QuestionBank, verbose_name='题目')
    class_name = models.ForeignKey(Class, verbose_name='班级')
    teacher = models.ForeignKey(Teacher, verbose_name='教师')
    is_bonus = models.CharField(max_length=1, choices=IS_BONUS, default='0', verbose_name='加分题')
    refer_complete_time = models.CharField(max_length=5, default='10', verbose_name='参考完成时间(分钟数)')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '作业布置'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.question

    __str__ = __repr__


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, verbose_name='作业')
    is_complete = models.CharField(max_length=1, choices=IS_COMPLETE, default='0', verbose_name='题目状态')
    complete_time = models.CharField(max_length=5, default='0', verbose_name='完成时间(分钟数)')
    py_file_path = models.CharField(max_length=200, default='', verbose_name='.py文件路径')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '作业提交'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.is_complete

    __str__ = __repr__
