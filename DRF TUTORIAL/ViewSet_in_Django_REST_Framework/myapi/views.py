from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("**********LIST***********")
        print("Baseman        =", self.basename)
        print("Action         =", self.action)
        print("Details        =", self.detail)
        print("Suffiex        =", self.suffix)
        print("Name           =", self.name)
        print("Discription    =", self.description)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("**********RETRIEVE***********")
        print("Baseman        =", self.basename)
        print("Action         =", self.action)
        print("Details        =", self.detail)
        print("Suffiex        =", self.suffix)
        print("Name           =", self.name)
        print("Discription    =", self.description)
        id = pk
        if id is not None:
            student = Student.objects.get(pk=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    def create(self, request):
        print("**********CREATE***********")
        print("Baseman        =", self.basename)
        print("Action         =", self.action)
        print("Details        =", self.detail)
        print("Suffiex        =", self.suffix)
        print("Name           =", self.name)
        print("Discription    =", self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print("**********UPDATE***********")
        print("Baseman        =", self.basename)
        print("Action         =", self.action)
        print("Details        =", self.detail)
        print("Suffiex        =", self.suffix)
        print("Name           =", self.name)
        print("Discription    =", self.description)
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print("**********PARTIAL UPDATE***********")
        print("Baseman        =", self.basename)
        print("Action         =", self.action)
        print("Details        =", self.detail)
        print("Suffiex        =", self.suffix)
        print("Name           =", self.name)
        print("Discription    =", self.description)
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        print("**********DELETE***********")
        print("Baseman        =", self.basename)
        print("Action         =", self.action)
        print("Details        =", self.detail)
        print("Suffiex        =", self.suffix)
        print("Name           =", self.name)
        print("Discription    =", self.description)
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_202_ACCEPTED)
