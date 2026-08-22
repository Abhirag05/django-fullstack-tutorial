from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#from drf_spectacular.utils import extend_schema 
'''
#function-based views for CRUD operations on Student model,which is useful for smaller applications or when you want to have more control over the request and response handling.with the help of api_view decorator.

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@extend_schema(request=StudentSerializer, responses=StudentSerializer)#for adding the schema for the add_student endpoint in swagger documentation
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=StudentSerializer, responses=StudentSerializer)
@api_view(['PUT','PATCH'])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='PATCH':#Allow partial updates, so if the request method is PATCH, we set partial=True in the serializer. This allows us to update only the fields that are provided in the request data, while leaving the other fields unchanged.
        serializer = StudentSerializer(student, data=request.data, partial=True)
    else:
        serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)#using get_object_or_404 to retrieve the student object based on the provided primary key (pk). If the student with the given pk does not exist, it will return a 404 Not Found response.its simplified version of the try-except block used in the update_student function.
    student.delete()
    return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)'''