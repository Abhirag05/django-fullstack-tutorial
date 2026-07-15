from django.urls import path
from . import views

urlpatterns=[
    path('shop-home/', views.home, name="shop-home"),
    path('shop-about/', views.shop, name="shop-about"),
]