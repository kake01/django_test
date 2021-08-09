from django.urls import path
from .views import TodoView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoView)
# urlpatterns = [
#     path('', TodoView.as_view(), name='todo'),
# ]
 