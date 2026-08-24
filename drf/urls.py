from django.urls import path
#from .views import student_list,add_student,update_student,delete_student
#from .views import StudentApi

"""urlpatterns = [
    #these are the urls needed for performing crud operations for function based views on student model
    #path('students/', student_list, name='student-list'),
    #path('students/add/', add_student, name='add-student'),
    #path('students/update/<int:pk>/', update_student, name='update-student'),
    #path('students/delete/<int:pk>/', delete_student, name='delete-student')'''

    #urls neded for performing crud operations for class based views on student model
    path('students/', StudentApi.as_view()),#for retrieving all students or adding a new student. 
    path('students/<int:pk>/', StudentApi.as_view()),#foor retrieving, updating, or deleting a specific student based on the provided primary key (pk).
]"""
from .views import StudentListCreateView,StudentRetrieveUpdateDestroyView
#urls for the class based generic api view + mixin views for performing CRUD operations on student model
urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), ),
]