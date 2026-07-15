from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the shop index.")

def shop(request):
    return HttpResponse("Hello, world. You're at the shops page.")

def product_details(request,id):
    return HttpResponse(f"Product detail page of id:{id}")