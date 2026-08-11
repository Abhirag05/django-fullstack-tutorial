from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile 
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

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, 'Your account has been created! You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login_view')

@login_required(login_url='login_view')
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required(login_url='login_view')
def upload_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_view')
        else:
            messages.error(request, 'Profile update failed. Please correct the error below.')
    else:
        form = UserProfileForm()
    return render(request, 'users/upload_profile.html', {'form': form})

@login_required(login_url='login_view')
def profile_view(request):
    profile = Profile.objects.all()
    return render(request, 'users/profile.html', {'profile': profile})