from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Message

class MessageView(TemplateView):
    def __init__(self):
        self.params = {
        }

    def get(self, request):
        data = Message.objects.all()
        self.params = {
            'data': data,
        }
        return render(request, 'chat/index.html', self.params)

    def post(self, request):
        return render(request, 'chat/index.html',self.params)