import xadmin
from .models import Assignment, Submission


class AssignmentAdmin(object):
    list_display = ['question', 'class_name', 'teacher', 'is_bonus', 'refer_complete_time', 'created_time']
    search_fields = ['question__title', 'class_name__name', 'teacher__name', 'is_bonus', 'refer_complete_time']
    list_filter = ['question', 'class_name', 'teacher', 'is_bonus', 'refer_complete_time', 'created_time']


class SubmissionAdmin(object):
    list_display = ['assignment', 'file_path', 'is_complete', 'complete_time', 'created_time']
    search_fields = ['assignment', 'file_path', 'is_complete', 'complete_time']
    list_filter = ['assignment', 'file_path', 'is_complete', 'complete_time', 'created_time']


xadmin.site.register(Assignment, AssignmentAdmin)
xadmin.site.register(Submission, SubmissionAdmin)
