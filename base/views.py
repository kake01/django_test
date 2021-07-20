from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    def __init__(self):
        self.params = {
            # 'goto': 'chat_bot_message',
        }
    
    # @login_required
    def get(self, request):
        self.params = {
            'chat': 'chat_bot_message',
            'todo': 'todo',
        }
        return render(request, 'base/home.html', self.params)

    # @login_required
    # def post(self, request):
    #     return redirect(to="/chat")
