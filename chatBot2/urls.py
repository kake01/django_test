from django.contrib import admin
from django.urls import path,include


from django.conf.urls import url# //includeを追記
from todo.urls import router as to_do_router#　//追記

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('base.urls')),
    path('chat/', include('chat.urls')),
    # path('todo/', include('todo.urls')),
    # url(r'^api/', include(to_do_router.urls)), #//追記
    url('todo/', include(to_do_router.urls)), #//追記
]
