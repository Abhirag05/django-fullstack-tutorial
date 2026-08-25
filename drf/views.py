#from rest_framework.views import APIView
#from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework import status
#from drf_spectacular.utils import extend_schema 
'''1st type of view

#function-based views with api_view decorator for CRUD operations on Student model,which is useful for smaller applications or when you want to have more control over the request and response handling.
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

"""
2nd type of views:

#Class based APIView for CRUD operations which is used when we need more control over the code ,typically used for custom apis .for simple crud avoid this and use ModelViewset or concrete GenericApiView.

class StudentApi(APIView):
    #for retrieving all students or a specific student based on the provided primary key (pk). If pk is None, it retrieves all students; otherwise, it retrieves the student with the given pk. The retrieved data is serialized using the StudentSerializer and returned in the response.
    def get(self, request,pk=None):
        if pk is None:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)

    #for adding a new student. It takes the request data, serializes it using the StudentSerializer, and checks if the serialized data is valid. If valid, it saves the new student to the database and returns the serialized data with a 201 Created status. If not valid, it returns the validation errors with a 400 Bad Request status.
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #for updating the entire record of a student object based on the provided primary key (pk). It retrieves the student object using get_object_or_404, serializes the request data along with the existing student object, and checks if the serialized data is valid. If valid, it saves the updated student to the database and returns the serialized data with a 200 OK status. If not valid, it returns the validation errors with a 400 Bad Request status.
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #for updating a specific field of a student object based on the provided primary key (pk). 
    def patch(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #for deleting a student object based on the provided primary key (pk). It retrieves the student object using get_object_or_404, deletes it from the database, and returns a success message with a 204 No Content status.
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)"""


"""
3rd type of view:

#drf generic api view + mixin views ,we have more control than concrete GenericAPIView but less than APIView.use when we need custom crud operations which doesnt provided by concrete generic api view.ie if we only need list and destroy kinda things

from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

#class based generic api view + mixin views for getting the entire list of students and adding a new student to the database. 
class StudentListCreateView(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #for getting the entire data
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #for adding a new student to the database
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
#class based generic api view + mixin views for retrieving, updating, or deleting a specific student based on the provided primary key (pk).
class StudentRetrieveUpdateDestroyView(generics.GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #for retrieving a specific student based on the provided primary key (pk)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    #for updating a specific student based on the provided primary key (pk)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    #for deleting a specific student based on the provided primary key (pk)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""

#4th type of views:
#concrete generic api views:GenericAPIView have more control than ModelViewSet but less than others.Use this for standard crud operations only. we can use it where the entire crud operations is not needed
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 

#for creating and listing
class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#for retrieving, updating, and deleting
class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

"""#5th type of view
# Crud operations using model viewsets use only when all the crud operations are needed.ie,create,read,update,delete,retrieve all 5.it need a separe router to internally separate urls.

from rest_framework import viewsets

#entire crud operations can be done through just this much of code and mostly used for the time when only standard crud is neeeded and here we have less control over code
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer"""