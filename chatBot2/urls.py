from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('base.urls')),
    path('chat/', include('chat.urls')),
    path('todo/', include('todo.urls')),
]
