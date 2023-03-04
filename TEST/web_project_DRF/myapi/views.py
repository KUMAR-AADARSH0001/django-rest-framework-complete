from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from rest_framework.response import Response
from .models import LogMessage
from .serializers import LogMessageSerializer
from django.shortcuts import redirect
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework import status
import datetime


print("http://127.0.0.1:8000/hello/VSCode/")


@api_view(['GET', 'POST'])
def homelistview(request):
    "get all avielable logs"
    if request.method == 'GET':
        logs = LogMessage.objects.all()
        serializer = LogMessageSerializer(logs, many=True)
        return Response({'status': True, 'data': serializer.data, 'message': 'Success'})

    if request.method == 'POST':
        data = request.data
        data['log_date'] = datetime.datetime.now()
        serializer = LogMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': serializer.data, 'message': 'Data created'}, status=status.HTTP_201_CREATED)
