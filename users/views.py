from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile 
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
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
    existing_profile = Profile.objects.filter(user=request.user).first()
        
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=existing_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_view')
        else:
            messages.error(request, 'Profile update failed. Please correct the error below.')
    else:
        form = UserProfileForm(instance=existing_profile)
    return render(request, 'users/upload_profile.html', {'form': form})

@login_required(login_url='login_view')
def profile_view(request):
    profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'users/profile.html', {'profile': profile})

def set_session(request):
    request.session['name'] = 'Abhirag'
    request.session['age'] = 20
    return HttpResponse("Session data set.")

def get_session(request):
    name = request.session.get('name', 'Guest')
    age = request.session.get('age', 'Unknown')
    return HttpResponse(f" Welcome, {name}! You are {age} years old.")

def delete_session(request):
    '''try:
        del request.session['name']
        del request.session['age']
        return HttpResponse("Session data deleted.")
    except KeyError:
        return HttpResponse("No session data to delete.")'''
    request.session.flush()
    return HttpResponse("All session data deleted.")

def set_cookie(request):
    response = HttpResponse("Cookie has been set.")
    response.set_cookie('name', 'Abhirag', max_age=3600)  # Cookie expires in 1 hour
    response.set_cookie('course','bca', max_age=3600)
    return response

def get_cookie(request):
    name = request.COOKIES.get('name', 'Guest')
    course = request.COOKIES.get('course', 'Unknown')
    return HttpResponse(f"Welcome, {name}! You are enrolled in {course}.")

def delete_cookie(request):
    response = HttpResponse("Cookie has been deleted.")
    response.delete_cookie('name')
    response.delete_cookie('course')
    return response

def send_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = 'from@example.com'
    recipient_list = ['test@example.com']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Email sent successfully.")

#email using html template
def send_html_email(request):
    subject = 'HTML Email Test'
    from_email = 'from@example.com'
    recipient_list = ['test@example.com']
    message = render_to_string('users/html_email.html', {'user': request.user})
    send_mail(subject, message, from_email, recipient_list, html_message=message)
    return HttpResponse("HTML email sent successfully.")