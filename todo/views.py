from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Todo

import django_filters
from rest_framework import viewsets, filters
from .serializer import TodoSerializer
from rest_framework.decorators import api_view


# class TodoView(TemplateView):
#     def __init__(self):
#         self.params = {
#         }

#     def get(self, request):
#         self.params = {
#             # 'data': data,
#         }
#         return render(request, 'todo/index.html', self.params)

#     # def post(self, request):
#     #    return render(request, 'todo/index.html', self.params)
    
class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-pub_date')
    serializer_class = TodoSerializer