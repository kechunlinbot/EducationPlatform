import xadmin

<<<<<<< Updated upstream
from .models import TeachersModel
=======
from .models import Teacher
>>>>>>> Stashed changes


class TeachersAdmin(object):
    list_display = ['name', 'real_name', 'email', 'class_teacher', 'add_time']
    search_fields = ['name', 'real_name', 'email', 'class_teacher__name']
    list_filter = ['name', 'real_name', 'email', 'class_teacher', 'add_time']


<<<<<<< Updated upstream
xadmin.site.register(TeachersModel, TeachersAdmin)
=======
xadmin.site.register(Teacher, TeachersAdmin)
>>>>>>> Stashed changes
