from django.urls import path
from .views import student_list

urlpatterns = [
    path('get-students/', student_list, name='student-list'),
]