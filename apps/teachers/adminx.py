import xadmin


from .models import Teacher


class TeachersAdmin(object):
    list_display = ['name', 'real_name', 'email', 'class_teacher', 'add_time']
    search_fields = ['name', 'real_name', 'email', 'class_teacher__name']
    list_filter = ['name', 'real_name', 'email', 'class_teacher', 'add_time']


xadmin.site.register(Teacher, TeachersAdmin)