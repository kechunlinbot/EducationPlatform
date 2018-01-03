import xadmin

<<<<<<< Updated upstream
from .models import HomeWorkModel

class HomeWorkAdmin(object):
    list_display = ['name', 'content','class_work', 'add_time']
    search_fields = ['name', 'content','class_work__name']
    list_filter = ['name', 'content','class_work', 'add_time']

xadmin.site.register(HomeWorkModel, HomeWorkAdmin)
=======
# from .models import HomeWork
#
# class HomeWorkAdmin(object):
#     list_display = ['name', 'content','class_work', 'add_time']
#     search_fields = ['name', 'content','class_work__name']
#     list_filter = ['name', 'content','class_work', 'add_time']
#
# xadmin.site.register(HomeWork, HomeWorkAdmin)
>>>>>>> Stashed changes
