from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo

# Create your views here.

def todo_list(request):
    todo_data=Todo.objects.all()
    return render(request,'todo/todo_list.html', {'todo_data': todo_data})

def todo_create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        if title and description:
            Todo.objects.create(title=title,description=description,completed=completed)
            messages.success(request, "Todo created successfully!")
            return redirect('todo:todo_list')
        else:
            messages.error(request, "Title and Description are required fields.")
            return redirect('todo:todo_list')
    return render(request,'todo/create_todo.html')

def todo_update(request, pk):
    todo=get_object_or_404(Todo, pk=pk)
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        if title and description:
            todo.title=title
            todo.description=description
            todo.completed = completed
            todo.save()
            messages.success(request, "Todo updated successfully!")
            return redirect('todo:todo_list')
        else:
            messages.error(request, "Title and Description are required fields.")
            return redirect('todo:todo_list')
    return render(request,'todo/create_todo.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        messages.success(request, "Todo deleted successfully!")
        return redirect('todo:todo_list')
    return render(request, 'todo_delete.html', {'todo': todo})

def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if todo:
        todo.completed = not todo.completed
        todo.save()
        messages.success(request, "Todo status updated successfully!")
    return redirect('todo:todo_list')