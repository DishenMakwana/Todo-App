from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect
from django.db import IntegrityError

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request,'main/index.html' , {'todo_items':todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    text_content = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date , text = text_content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request , todo_id):
    if request.method =="POST": 
        Todo.objects.get(id = todo_id).delete()
        return HttpResponseRedirect("/")

    return render(request, "index.html")
    
