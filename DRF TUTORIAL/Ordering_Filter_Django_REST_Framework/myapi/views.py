from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
# Create your views here.


class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    "if you not give ordering_feilds then it will ordered with any of fields"
    # ordering_fields = ['name']  # it will ordered with name
    ordering_fields = ['name', 'city']  # it will ordered with name and city
