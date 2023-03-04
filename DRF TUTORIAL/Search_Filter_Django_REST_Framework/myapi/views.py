from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city']  # this is search by city
    search_fields = ['name', 'city']  # this is search by name or city
    # search_fields = ['^name']  # this is search by startwith
    # search_fields = ['=']  # this is search by exect search value
