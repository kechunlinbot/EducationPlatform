# 140.143.189.20  2017yuanzhi
#
from django.shortcuts import render, HttpResponse
from .models import Submission, Assignment
from django.views.generic import View, ListView
from knowledgequestions.models import Course
from classes.models import Class
from knowledgequestions .models import Module, KnowledgeBase, QuestionBank
import json

# Create your views here.

class PublishView(View):
    def get(self, request):
        #print('hello world!', '&'*100)
        course_name = request.GET.get('q')
        course = Course.objects.filter(name=course_name)
        modules = Module.objects.filter(course=course)
        module_dict = {}
        for module in modules:
            module_name = module.name
            print(module_name)
            module_dict['%s'% module_name] = module_name
            print(module_dict)
        return HttpResponse(json.dumps(module_dict), content_type="application/json")

def submit_module_info(request):
    if request.method == 'GET':
        module_name = request.GET.get('q')
        print(module_name)
        module = Module.objects.filter(name = module_name)
        knowledgebases = KnowledgeBase.objects.filter(module=module)
        info = {'en_name': request.session.get(id),
                'knowledgebases': knowledgebases
                }
        return render(request, 'publish_tasks.html', info)
    else:
        return render(request, 'publish_tasks.html')

def submit_knowledgebase_info(request):
    print('hello world')
    if request.method == 'GET':
        knowledgebase_name = request.GET.get('q')
        print(knowledgebase_name)
        knowledgebase = KnowledgeBase.objects.filter(name=knowledgebase_name)
        print(knowledgebase)
        questionbanks = QuestionBank.objects.filter(knowledgebase=knowledgebase)
        print(questionbanks,'&'*100)
        info = {'en_name': request.session.get(id),
                'questionbanks': questionbanks
                }
        return render(request, 'publish_tasks.html', info)
    else:
        return render(request, 'publish_tasks.html')



class ViewTheDegreeOfCompletionView(View):
    def get(self, request):
        return render(request, 'view_the_degree_of_completion_tch.html')

class SubmitView(View):
    def get(self):
        pass

    def post(self):
        pass


