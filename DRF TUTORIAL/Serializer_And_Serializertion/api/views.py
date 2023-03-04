from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Model Object & Single Student Data


def student_detail(request, pk=None):
    "It will give all data of student id=1"
    stu_data = Student.objects.get(id=pk)
    # print(stu_data)
    "It will convert complexx data to python data"
    serializer = StudentSerializer(stu_data)
    # print(serializer)
    # print(serializer.data)
    "It will convert python data to json data"
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    "By defaul its content type not set"
    return HttpResponse(json_data, content_type='application/json')


# Query Set - All Student Data
@csrf_exempt
def student_list(request):
    "It will give all data in student list"
    stu_data = Student.objects.all()
    # print(stu_data)
    "It will convert complexx data to python data"
    serializer = StudentSerializer(stu_data, many=True)
    # print(serializer)
    # print(serializer.data)
    # "It will convert python data to json data"
    # json_data = JSONRenderer().render(serializer.data)
    # # print(json_data)
    # "By defaul its content type not set"
    # return HttpResponse(json_data, content_type='application/json')
    "if you don't want to write uper two line so write this"
    return JsonResponse(serializer.data, safe=False)
