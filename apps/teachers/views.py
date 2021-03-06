#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : dengguo

from django.shortcuts import render
from django.views.generic import View
from .forms import TchRegForm, TchInfoForm, TchLogForm
from .models import Teacher
from django.contrib.auth.hashers import make_password, check_password
from knowledgequestions.models import Course
from classes.models import Class
from knowledgequestions .models import Module, KnowledgeBase, QuestionBank

# Create your views here.
def homepage_tch(request):
    return render(request, 'home_page_tea.html')

class TchRegisterView(View):
    def get(self, request):
        return render(request, 'register_info_tea.html', {})

    def post(self, request):
        tch_reg_form = TchRegForm(request.POST)
        if tch_reg_form.is_valid():
            en_name = tch_reg_form.cleaned_data['en_name']
            passwd = tch_reg_form.cleaned_data['passwd']
            teacher = Teacher.objects.filter(en_name=en_name)
            if teacher:  # 用户名已存在
                return render(request, 'register_info_tea.html', {'msg': '用户名已存在'})
            return render(request, 'basic_info_tea.html', {'en_name': en_name,
                                                           'passwd': passwd})
        else:
            return render(request, 'register_info_tea.html', {'tch_reg_form': tch_reg_form})

class TchRegisterInfoView(View):
    def post(self, request):
        tch_info_form = TchInfoForm(request.POST)
        if tch_info_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            real_name = tch_info_form.cleaned_data['real_name']
            gender = tch_info_form.cleaned_data['gender']
            degree = tch_info_form.cleaned_data['degree']
            school = tch_info_form.cleaned_data['school']
            major = tch_info_form.cleaned_data['major']
            email = tch_info_form.cleaned_data['email']

            teacher = Teacher()
            teacher.en_name = en_name
            teacher.passwd = make_password(passwd, 'dengguo', 'pbkdf2_sha256')
            teacher.real_name = real_name
            teacher.school = school
            teacher.gender = gender
            teacher.degree = degree
            teacher.major = major
            teacher.email = email
            teacher.save()
            return render(request, 'log_in_tea.html')
        else:
            return render(request, 'basic_info_tea.html', {'tch_info_form': tch_info_form})


class TchLoginView(View):
    def get(self, request):
        return render(request, 'log_in_tea.html', {})

    def post(self, request):
        tch_log_form = TchLogForm(request.POST)
        if tch_log_form.is_valid():
            en_name = tch_log_form.cleaned_data['en_name']
            passwd = tch_log_form.cleaned_data['passwd']
            teachers = Teacher.objects.filter(en_name=en_name)
            if teachers:
                for teacher in teachers:
                    result = check_password(passwd, teacher.passwd)
                    print(result)
                    if result == 1:
                        request.session['teacher_id'] = teacher.id

                        classes = Class.objects.all()
                        courses = Course.objects.all()
                        info = {
                            'classes':classes,
                            'courses':courses,
                            'en_name':en_name,
                        }
                        return render(request, 'publish_tasks.html', info)
                    else:
                        return render(request, 'log_in_tea.html', {'tch_log_form': tch_log_form})
            else:
                return render(request, 'register_info_tea.html')


def logout_tch(request):
    try:
        del request.session['teacher_id']
    except KeyError as e:
        print(e)
    return render(request, 'home_page_tea.html')