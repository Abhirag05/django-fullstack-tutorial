from django.shortcuts import render
from .models import Todo

# Create your views here.

def todo_list(request):
    todo_data=Todo.objects.all()
    return render(request,'todo/todo_list.html', {'todo_data': todo_data})

def todo_create(request):
    return render(request,'todo/todo_create.html')

def todo_update(request, pk):
    return render(request,'todo/todo_update.html')

def todo_delete(request, pk):
    return render(request,'todo/todo_delete.html')