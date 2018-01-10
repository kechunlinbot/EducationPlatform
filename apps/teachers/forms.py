# @author shi.qi.chang
from django import forms


class TchRegForm(forms.Form):
    """教师注册信息表单类"""
    en_name = forms.CharField(min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)


class TchLogForm(forms.Form):
    """教师登录信息表单类"""
    en_name = forms.CharField(min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)


class TchInfoForm(forms.Form):
    """教师基本信息表单类"""
    en_name = forms.CharField(min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)
    real_name = forms.CharField(min_length=2, max_length=20)
    gender = forms.CharField(required=True)
    degree = forms.CharField(required=True)
    major = forms.CharField(max_length=30, required=True)
    school = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
