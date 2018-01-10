import xadmin
from .models import Course, Module, KnowledgeBase, QuestionBank


class CourseAdmin(object):
    list_display = ['name', 'detail', 'difficulty_level', 'category', 'creator', 'modifier', 'created_time',
                    'modified_time']
    search_fields = ['name', 'detail', 'difficulty_level', 'category', 'creator', 'modifier']
    list_filter = ['name', 'detail', 'difficulty_level', 'category', 'creator', 'modifier', 'created_time',
                   'modified_time']


class ModuleAdmin(object):
    list_display = ['course', 'name', 'created_time']
    search_fields = ['course__name', 'name']
    list_filter = ['course', 'name', 'created_time']


class KnowledgeBaseAdmin(object):
    list_display = ['module', 'name', 'knowledge_point', 'created_time']
    search_fields = ['module__name', 'name', 'knowledge_point']
    list_filter = ['module', 'name', 'knowledge_point', 'created_time']


class QuestionBankAdmin(object):
    list_display = ['title', 'content', 'difficulty_level', 'module', 'created_time']
    search_fields = ['title', 'content', 'difficulty_level', 'module__name']
    list_filter = ['title', 'content', 'difficulty_level', 'module', 'created_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Module, ModuleAdmin)
xadmin.site.register(KnowledgeBase, KnowledgeBaseAdmin)
xadmin.site.register(QuestionBank, QuestionBankAdmin)
