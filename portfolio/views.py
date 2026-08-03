from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Contact
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            return HttpResponse(f"Thank you {name} for your message!")
        else:
            return HttpResponse("Please fill in all fields.")
    return redirect('contact')