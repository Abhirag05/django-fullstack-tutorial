from django.urls import path
from .views import student_list,add_student

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/add/', add_student, name='add-student')

]