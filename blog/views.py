from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import BlogForm
from django.contrib import messages
from .models import Blog 
# Create your views here.
def home(request):
    return render(request,'blogs/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the blog about page.")

def article_by_year(request,year):
    return HttpResponse(f"Article from the year: {year}")

def article_details(request,**kwargs):
    return HttpResponse(f"Article from the year: {kwargs['year']} and month:{kwargs['month']}")

#Filters example
def article_filter(request):
    blogs=[
        {"title": "Blog 1", "is_featured": True, "author": "Author 1"},
        {"title": "Blog 2", "is_featured": False, "author": "Author 2"},
        {"title": "Blog 3", "is_featured": False, "author": "Author 3"}
    ]
    post_list ={
            "blogs": blogs,
            "title": "Post 1",
            "author": "Author 1",
            "date": datetime(2025, 8, 1),
            "content": "This is the content of the post.",
            "price": 100,
            "test": "<b>Auto escape example</b>",
        }
    return render(request, 'blogs/article_filter.html', {'post_list': post_list})

def create_blog(request):
    form=BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog created successfully!")
            return redirect('blog:create_blog')
    return render(request, 'blogs/create_blog.html', {'form': form})