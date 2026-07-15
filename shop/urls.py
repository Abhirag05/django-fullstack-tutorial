from django.urls import path
from . import views

urlpatterns=[
    path('shop-home/', views.home, name="shop-home"),
    path('shop-about/', views.shop, name="shop-about"),
    path('shop-about/<int:id>/',views.product_details,name="product-detail"),
]