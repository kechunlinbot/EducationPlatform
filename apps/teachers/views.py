from django.shortcuts import render
from django.views.generic import View
from .forms import TchRegForm, TchInfoForm, TchLogForm
from .models import Teacher
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def homepage_tch(request):
    return render(request, 'home_page_tea.html')


class TchRegisterView(View):
    def get(self, request):
        return render(request, 'register_info_tea.html', {})

    def post(self, request):
        tch_reg_form = TchRegForm(request.POST)
        if tch_reg_form.is_valid():
            name = tch_reg_form.cleaned_data['name']
            password = tch_reg_form.cleaned_data['password']
            student = Teacher.objects.filter(name=name)
            if student:  # 用户名已存在
                return render(request, 'register_info_tea.html', {'msg': '用户名已存在'})
            return render(request, 'basic_info_tea.html', {'name': name,
                                                           'password': password})
        else:
            return render(request, 'register_info_tea.html', {'tch_reg_form': tch_reg_form})


class TchRegisterInfo(View):
    def post(self, request):
        tch_info_form = TchInfoForm(request.POST)
        if tch_info_form.is_valid():
            name = tch_info_form.cleaned_data['name']
            password = tch_info_form.cleaned_data['password']
            real_name = tch_info_form.cleaned_data['real_name']
            gender = tch_info_form.cleaned_data['gender']
            degree = tch_info_form.cleaned_data['degree']
            school = tch_info_form.cleaned_data['school']
            major = tch_info_form.cleaned_data['major']
            email = tch_info_form.cleaned_data['email']

            teacher = Teacher()
            teacher.name = name
            teacher.password = make_password(password)
            teacher.real_name = real_name
            teacher.school = school
            teacher.gender = gender
            teacher.degree = degree
            teacher.major = major
            teacher.email = email
            teacher.save()
            return render(request, 'log_in_tea.html', {})
        else:
            return render(request, 'basic_info_tea.html', {'tch_info_form': tch_info_form})


class TchLoginView(View):
    def get(self, request):
        return render(request, 'log_in_tea.html', {})

    def post(self, request):
        tch_log_form = TchLogForm(request.POST)
        if tch_log_form.is_valid():
            name = tch_log_form.cleaned_data['name']
            password = tch_log_form.cleaned_data['password']
            teacher = Teacher.objects.filter(name=name)
            if teacher:
                hash_password = make_password(password)
                result = check_password(teacher.password, hash_password)
                if result == 1:
                    request.session['teacher_id'] = teacher.id
                    return render(request, '')
                else:
                    return render(request, 'log_in_tea.html', {'tch_log_form': tch_log_form})
            else:
                return render(request, 'register_info_tea.html', {})


def logout_tch(request):
    try:
        del request.session['teacher_id']
    except KeyError as e:
        print(e)
    return render(request, 'home_page_tea.html', {})
