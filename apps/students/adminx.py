import xadmin

<<<<<<< Updated upstream
from .models import StudentsModel
=======
from .models import Student
>>>>>>> Stashed changes


class StudentsAdmin(object):
    list_display = ['real_name', 'name', 'gender', 'mobile', 'class_student', 'add_time']
    search_fields = ['real_name', 'name', 'gender', 'mobile', 'class_student__name']
    list_filter = ['real_name', 'name', 'gender', 'mobile', 'class_student', 'add_time']


<<<<<<< Updated upstream
xadmin.site.register(StudentsModel, StudentsAdmin)
=======
xadmin.site.register(Student, StudentsAdmin)
>>>>>>> Stashed changes
