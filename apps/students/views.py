from django.shortcuts import render
from django.views.generic import View
from .forms import StuRegForm, StuInfoForm, StuLogForm
from .models import StudentsModel
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def homepage_stu(request):
    return render(request, 'home_page_stu.html')

class StuRegisterView(View):
    def get(self, request):
        return render(request, 'register_info_stu.html', {})

    def post(self, request):
        stu_reg_form = StuRegForm(request.POST)
        if stu_reg_form.is_valid():
            name = stu_reg_form.cleaned_data['name']
            password = stu_reg_form.cleaned_data['password']
            student = StudentsModel.objects.filter(name=name)
            if student: # 用户名已存在
                return render(request, 'register_info_stu.html', {'msg': '用户名已存在'})
            return render(request, 'basic_info_stu.html', {'name': name,
                                                           'password': password})
        else:
            return render(request, 'register_info_stu.html', {'stu_reg_form': stu_reg_form})


class StuRegisterInfo(View):
    def post(self, request):
        stu_info_form = StuInfoForm(request.POST)
        if stu_info_form.is_valid():
            name = stu_info_form.cleaned_data['name']
            password = stu_info_form.cleaned_data['password']
            real_name = stu_info_form.cleaned_data['real_name']
            mobile = stu_info_form.cleaned_data['mobile']
            gender = stu_info_form.cleaned_data['gender']
            height = stu_info_form.cleaned_data['height']
            weight = stu_info_form.cleaned_data['weight']
            degree = stu_info_form.cleaned_data['degree']
            learning = stu_info_form.cleaned_data['learning']
            allergies = stu_info_form.cleaned_data['allergies']

            student = StudentsModel()
            student.name = name
            student.password = make_password(password)
            student.real_name = real_name
            student.mobile = mobile
            student.gender = gender
            student.height = height
            student.weight = weight
            student.degree = degree
            student.learning = learning
            student.allergies = allergies
            student.save()
            return render(request, 'basic_info_stu.html', )
        else:
            return render(request, 'basic_info_stu.html', {'stu_info_form': stu_info_form})

class StuLoginView(View):
    def get(self, request):
        return render(request, 'log_in_stu.html', {})

    def post(self, request):
        stu_log_form = StuLogForm(request.POST)
        if stu_log_form.is_valid():
            name = stu_log_form.cleaned_data['name']
            password = stu_log_form.cleaned_data['password']
            student = StudentsModel.objects.filter(name=name)
            if student:
                hash_password = make_password(password)
                result = check_password(student.password, hash_password)
                if result == 1:
                    request.session['student_id'] = student.id
                    return render(request, '')
                else:
                    return render(request, 'log_in_stu.html', {'stu_log_form':stu_log_form})
            else:
                return render(request, 'register_info_stu.html', {})

def logout_stu(request):
    try:
        del request.session['student_id']
    except KeyError as e:
        print(e)
    return render(request, 'log_in_stu.html', {})

