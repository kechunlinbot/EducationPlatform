import xadmin

<<<<<<< Updated upstream
from .models import ClassModel
=======
from .models import Class
>>>>>>> Stashed changes

class ClassAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


<<<<<<< Updated upstream
xadmin.site.register(ClassModel, ClassAdmin)
=======
xadmin.site.register(Class, ClassAdmin)
>>>>>>> Stashed changes
