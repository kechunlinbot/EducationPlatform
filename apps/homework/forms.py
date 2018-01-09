# @author shi.qi.chang
from django import forms


class AssignmentsForm(forms.Form):
    """老师作业布置表单类"""
    class_name = forms.CharField(required=True)
    course = forms.CharField(required=True)
    first_module = forms.CharField(required=True)
    second_module = forms.CharField(required=True)
    is_bonus = forms.CharField(required=True)
    is_release = forms.CharField(required=True)


class CompletionForm(forms.Form):
    """作业完成度表单类"""
    class_name = forms.CharField(required=True)
    course = forms.CharField(required=True)
    created_time = forms.CharField(required=True)


class FileForm(forms.Form):
    """文件上传表单类"""
    file = forms.FileField()
