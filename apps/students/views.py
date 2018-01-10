from django.shortcuts import render
from django.views.generic import View
from .forms import StuRegForm, StuInfoForm, StuLogForm
from .models import Student
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def homepage_stu(request):
    return render(request, 'home_page_stu.html')

class StuRegisterView(View):
    def get(self, request):
        return render(request, 'register_info_stu.html')

    def post(self, request):
        stu_reg_form = StuRegForm(request.POST)
        if stu_reg_form.is_valid():
            en_name = stu_reg_form.cleaned_data['en_name']
            passwd = stu_reg_form.cleaned_data['passwd']
            student = Student.objects.filter(en_name=en_name)
            print('*' * 50, en_name, passwd)
            if student:             # 用户名已存在
                return render(request, 'register_info_stu.html', {'msg': '用户名已存在'})
            return render(request, 'basic_info_stu.html', {'en_name': en_name,
                                                           'passwd': passwd})
        else:
            return render(request, 'register_info_stu.html', {'stu_reg_form': stu_reg_form})


class StuRegisterInfoView(View):
    def post(self, request):
        stu_info_form = StuInfoForm(request.POST)
        if stu_info_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            real_name = stu_info_form.cleaned_data['real_name']
            mobile = stu_info_form.cleaned_data['mobile']
            gender = stu_info_form.cleaned_data['gender']
            height = stu_info_form.cleaned_data['height']
            weight = stu_info_form.cleaned_data['weight']
            degree = stu_info_form.cleaned_data['degree']
            learning = stu_info_form.cleaned_data['learning']
            allergies = stu_info_form.cleaned_data['allergies']

            student = Student()
            student.en_name = en_name
            student.passwd = make_password(passwd, 'dengguo', 'pbkdf2_sha256')
            student.real_name = real_name
            student.mobile = mobile
            student.gender = gender
            student.height = height
            student.weight = weight
            student.degree = degree
            student.learning = learning
            student.allergies = allergies
            student.save()
            return render(request, 'log_in_stu.html' )
        else:
            return render(request, 'basic_info_stu.html', {'stu_info_form': stu_info_form})

class StuLoginView(View):
    def get(self, request):
        return render(request, 'log_in_stu.html')

    def post(self, request):
        stu_log_form = StuLogForm(request.POST)
        if stu_log_form.is_valid():
            en_name = stu_log_form.cleaned_data['en_name']
            passwd = stu_log_form.cleaned_data['passwd']
            students = Student.objects.filter(en_name=en_name)
            if students:
                for student in students:
                    result = check_password(passwd, student.passwd)
                    if result == 1:
                        request.session['student_id'] = student.id
                        return render(request, 'view_all_tasks_stu.html')
                    else:
                        return render(request, 'log_in_stu.html', {'stu_log_form':stu_log_form})
                else:
                    return render(request, 'register_info_stu.html')

def logout_stu(request):
    try:
        del request.session['student_id']
    except KeyError as e:
        print(e)
    return render(request, 'log_in_stu.html')

