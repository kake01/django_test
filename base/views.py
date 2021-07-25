from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    def __init__(self):
        self.params = {
        }
    
    def get(self, request):
        self.params = {
            'chat': 'chat_bot_message',
            'todo': 'todo',
        }
        return render(request, 'base/home.html', self.params)