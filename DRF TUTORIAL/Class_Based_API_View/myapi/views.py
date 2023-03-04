from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Data Created Successfully !!!...'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Complete Data Updated Successfully !!!...'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.erorrs, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Partial Data Updated Successfully !!!...'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.erorrs, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"success": True, 'msg': 'Data Deleted Successfully !!!...'}, status=status.HTTP_204_NO_CONTENT)
