from django.shortcuts import render

# Create your views here.

def todo_list(request):
    return render(request,'todo/todo_list.html')

def todo_create(request):
    return render(request,'todo/todo_create.html')

def todo_update(request, pk):
    return render(request,'todo/todo_update.html')

def todo_delete(request, pk):
    return render(request,'todo/todo_delete.html')