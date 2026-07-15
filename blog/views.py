from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def about(request):
    return HttpResponse("Hello, world. You're at the blog about page.")

def article_by_year(request,year):
    return HttpResponse(f"Article from the year: {year}")

def article_details(request,**kwargs):
    return HttpResponse(f"Article from the year: {kwargs['year']} and month:{kwargs['month']}")