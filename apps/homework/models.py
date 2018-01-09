# @author shi.qi.chang
from django.db import models
from django.utils import timezone

from classes.models import Class
from teachers.models import Teacher
from students.models import Student
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


def stu_directory_path(instance, filename):
        return '%s/%s' % (instance.student, filename)


class File(models.Model):
    student = models.ForeignKey(Student, verbose_name='学生')
    upload_file = models.FileField(upload_to=stu_directory_path, verbose_name='上传文件路径')
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    class Meta:
        verbose_name = '文件上传'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.upload_file

    __str__ = __repr__


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, verbose_name='题目')
    file_path = models.ForeignKey(File, null=True, blank=True, verbose_name='上传文件路径')
    is_complete = models.CharField(max_length=1, choices=IS_COMPLETE, default='0', verbose_name='题目状态')
    complete_time = models.CharField(max_length=5, default='0', verbose_name='完成时间(分钟数)')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '作业提交'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.file_path

    __str__ = __repr__
