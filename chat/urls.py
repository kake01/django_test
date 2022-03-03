from django.urls import path
from .views import MessageView
urlpatterns = [
    path('', MessageView.as_view(), name='chat_bot_message'),
]
 