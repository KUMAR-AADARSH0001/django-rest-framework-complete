from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Data Created Successfully !!!...'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Complete Data Updated Successfully !!!...'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Partial Data Updated Successfully !!!...'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"success": True, 'msg': 'Data Deleted Successfully !!!...'}, status=status.HTTP_201_CREATED)
