import xadmin

from .models import Student

class StudentsAdmin(object):
    list_display = ['real_name', 'en_name', 'gender', 'mobile', 'class_name', 'created_time']
    search_fields = ['real_name', 'en_name', 'gender', 'mobile', 'class_name__name']
    list_filter = ['real_name', 'en_name', 'gender', 'mobile', 'class_name', 'created_time']


xadmin.site.register(Student, StudentsAdmin)
