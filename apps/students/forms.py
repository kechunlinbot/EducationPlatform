# @author shi.qi.chang
from django import forms


class StuRegForm(forms.Form):
    """学生注册信息表单类"""
    en_name = forms.CharField(min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=50)


class StuLogForm(forms.Form):
    """学生登录信息表单类"""
    en_name = forms.CharField(min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=50)


class StuInfoForm(forms.Form):
    """学生基本信息表单类"""
    real_name = forms.CharField(min_length=2, max_length=20)
    mobile = forms.CharField(min_length=11, max_length=11)
    gender = forms.CharField(required=True)
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    degree = forms.CharField(required=True)
    learning = forms.CharField(max_length=200, min_length=20)
    allergies = forms.CharField(max_length=200, min_length=20)
