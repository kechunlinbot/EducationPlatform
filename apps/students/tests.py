from django.test import TestCase

# Create your tests here.

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import StudentsModel
from django.contrib.auth.hashers import make_password, check_password
from .forms import StuRegForm, StuInfoForm, StuLogForm


def home_page_stu(request):
    return render(request, 'home_page_stu.html')


def login_in_stu(request):
    if request.method == 'GET':
        return render(request, 'log_in_stu.html')
    else:
        stulogform = StuLogForm(request.POST)
        if stulogform.is_valid():
            name = stulogform.cleaned_data['name']
            password = stulogform.cleaned_data['password']
            students = StudentsModel.objects.all()
            for student in students:
                if student.name == name:
                    hash_password = make_password(password)
                    result = check_password(student.password, hash_password)
                    if result == 1:
                        request.session['student_id'] = student.id
                        return HttpResponseRedirect('登录成功')
                    else:
                        return HttpResponse('name or password incorreact, please insure')
                else:
                    return HttpResponse('name is not exits, please register first')


def logout(request):
    try:
        del request.session['student_id']
    except KeyError as e:
        print(e)
    return HttpResponse("You're logged out.")


def register_info_stu(request):
    if request.method == 'GET':
        return render(request, 'register_info_tea.html')
    else:
        sturegform = StuRegForm(request.POST)
        if sturegform.is_valid():
            name = sturegform.cleaned_data['name']
            password = sturegform.cleaned_data['password']
            reg_info = {
                name: name,
                password: password
            }
            return render(request, 'basic_info_stu.html', reg_info)


def base_info_stu(request):
    student = StudentsModel()
    stuinfoform = StuInfoForm(request.POST)
    if stuinfoform.is_valid():
        name = stuinfoform.cleaned_data['name']
        password = stuinfoform.cleaned_data['password']
        real_name = stuinfoform.cleaned_data['real_name']
        gender = stuinfoform.cleaned_data['gender']
        mobile = stuinfoform.cleaned_data['mobile']
        weight = stuinfoform.cleaned_data['weight']
        height = stuinfoform.cleaned_data['height']
        degree = stuinfoform.cleaned_data['degree']
        learning = stuinfoform.cleaned_data['learning']
        allergies = stuinfoform.cleaned_data['allergies']

        hash_password = make_password(password)
        student.name = name
        student.password = hash_password
        student.real_name = real_name
        student.gender = gender
        student.mobile = mobile
        student.weight = weight
        student.height = height
        student.degree = degree
        student.learning = learning
        student.allergies = allergies

        student.save()
        return HttpResponse('注册成功')
    else:
        pass
