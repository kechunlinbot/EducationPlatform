import xadmin

from .models import StudentsModel


class StudentsAdmin(object):
    list_display = ['real_name', 'name', 'gender', 'mobile', 'class_student', 'add_time']
    search_fields = ['real_name', 'name', 'gender', 'mobile', 'class_student__name']
    list_filter = ['real_name', 'name', 'gender', 'mobile', 'class_student', 'add_time']


xadmin.site.register(StudentsModel, StudentsAdmin)
