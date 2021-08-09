from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Todo
from .forms import  TodoForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class TodoView(TemplateView):
    def __init__(self):
        self.params = {
        }

    def get(self, request):
        self.params = {
            # 'data': data,
        }
        return render(request, 'todo/index.html', self.params)

    # def post(self, request):
    #    return render(request, 'todo/index.html', self.params)
    
 