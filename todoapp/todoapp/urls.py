from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from todolist.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/',include('todolist.urls')),
    #path('',index,name="TodoList"),
]
