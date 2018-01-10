"""EducationPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import xadmin
import students
from students.views import StuRegisterView, StuLoginView, StuRegisterInfoView, logout_stu
import teachers
from teachers.views import TchRegisterView, TchLoginView, TchRegisterInfoView, logout_tch
from homework.views import PublishView, SubmitView, ViewTheDegreeOfCompletionView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^homepage_stu/$' ,students.views.homepage_stu, name='homepage_stu'),
    url(r'^register_stu/$', StuRegisterView.as_view(), name="register_stu"),
    url(r'^register_info_stu/$', StuRegisterView.as_view(), name="register_info_stu"),
    url(r'^submit_register_info_stu/$', StuRegisterInfoView.as_view(), name="submit_register_info_stu"),
    url(r'^login_stu/$', StuLoginView.as_view(), name='login_stu'),
    url(r'^submit_login_info_stu/$', StuLoginView.as_view(), name='submit_login_info_stu'),
    url(r'^view_all_tasks/$', teachers.views.logout_tch, name='view_all_tasks'),
    url(r'^logout_stu/$', students.views.logout_stu),

    url(r'^homepage_tch/$', teachers.views.homepage_tch, name='homepage_tch'),
    url(r'^register_tch/$', TchRegisterView.as_view(), name="register_tch"),
    url(r'^register_info_tch/$', TchRegisterInfoView.as_view(), name="register_info_tch"),
    url(r'^submit_register_info_tch/$', TchRegisterInfoView.as_view(), name="submit_register_info_tch"),
    url(r'^login_tch/$', TchLoginView.as_view(), name='login_tch'),
    url(r'^submit_login_info_tch/$', TchLoginView.as_view(), name='submit_login_info_tch'),
    url(r'^publish_tasks/$', PublishView.as_view(), name='publish_tasks'),
    url(r'^view_the_degree_of_completion_tch/$', ViewTheDegreeOfCompletionView.as_view(), name='view_the_degree_of_completion_tch'),
    url(r'^view_detail_of_completion_tch/$', ViewTheDegreeOfCompletionView.as_view(), name='view_detail_of_completion_tch'),
    url(r'^logout_tch/$', teachers.views.logout_tch, name='logout_tch'),
]

