from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('messages/',views.show_messages,name="messages"),

]