import xadmin

from .models import Teacher


class TeachersAdmin(object):
    list_display = ['en_name', 'real_name', 'gender', 'email', 'created_time']
    search_fields = ['en_name', 'real_name', 'gender', 'email']
    list_filter = ['en_name', 'real_name', 'gender', 'email', 'created_time']


xadmin.site.register(Teacher, TeachersAdmin)
