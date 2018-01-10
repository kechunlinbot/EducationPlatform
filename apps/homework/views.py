from django.shortcuts import render
from .models import Submission, Assignment
from django.views.generic import View
from knowledgequestions.models import Course

# Create your views here.

class PublishView(View):
    def get(self, request):
        return render(request, 'publish_tasks.html')

    def post(self):
        pass

class ViewTheDegreeOfCompletionView(View):
    def get(self, request):
        return render(request, 'view_the_degree_of_completion_tch.html')

class SubmitView(View):
    def get(self):
        pass

    def post(self):
        pass


