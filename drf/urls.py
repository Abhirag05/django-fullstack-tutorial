from django.urls import path
#from .views import student_list,add_student,update_student,delete_student

urlpatterns = [
    '''#these are the urls needed for performing crud operations for function based views on student model
    path('students/', student_list, name='student-list'),
    path('students/add/', add_student, name='add-student'),
    path('students/update/<int:pk>/', update_student, name='update-student'),
    path('students/delete/<int:pk>/', delete_student, name='delete-student')'''
]