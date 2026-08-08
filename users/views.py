from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def home(request):

    context={
        'user':User('Abhi',21),
        'name':'Abhirag S V',
        'age' :20,
        'skills':['python','django','javascript'],
        'role':'Developer',
        'address':{
            'title':"My details",
            'city':'Bangalore',
            'state':'Karnataka',
        },
        'empty_value':None,
    }
    return render(request,'index.html',context)

def show_messages(request):
    messages.debug(request, 'This is a debug message.')
    messages.info(request, 'This is an info message.')
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')
    return render(request, 'users/messages.html')