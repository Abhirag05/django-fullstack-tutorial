from django.shortcuts import render
from django.http import HttpResponse
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