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
from students.views import StuRegisterView, StuLoginView
from students import views
import teachers
from teachers.views import TchRegisterView, TchLoginView
from teachers import views


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^register_stu/$', StuRegisterView.as_view(), name="register_stu"),
    url(r'^register_info_stu/$', StuRegisterView.as_view(), name="register_info_stu"),
    url(r'^homepage_stu/$' ,students.views.homepage_stu, name='homepage_stu'),
    url(r'^login_stu/$', StuLoginView.as_view(), name='login_stu'),
    url(r'^logout_stu/$', students.views.logout_stu),

    url(r'^register_tch/$', TchRegisterView.as_view(), name="register_tch"),
    url(r'^register_info_tch/$', TchRegisterView.as_view(), name="register_info_tch"),
    url(r'^homepage_tch/$', teachers.views.homepage_tch, name='homepage_tch'),
    url(r'^login_tch/$', StuLoginView.as_view(), name='login_tch'),
    url(r'^logout_tch/$', teachers.views.logout_tch),

]


