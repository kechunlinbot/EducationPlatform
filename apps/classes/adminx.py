import xadmin

from .models import ClassModel

class ClassAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


xadmin.site.register(ClassModel, ClassAdmin)