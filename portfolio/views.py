from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'portfolio/home.html',context)

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')