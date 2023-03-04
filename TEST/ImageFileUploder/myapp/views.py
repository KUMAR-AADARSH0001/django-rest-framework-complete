from django.shortcuts import render
from .models import ImageUploder
from django.http import HttpResponse
from .models import ImageUploder
from .serializers import StudentSerializer
# Create your views here.


def home(request):
    if request.method == "POST":
        form = ImageUploder(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('msg = Image Uploaded Successfully')
        return HttpResponse('msg = Somthing Went Wrong')


def get(request):
    if request.method == 'GET':
        stu = ImageUploder.objects.all()
        serializer = StudentSerializer(stu)
        return HttpResponse(serializer.data)
