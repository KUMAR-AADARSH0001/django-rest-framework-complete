from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission
# FOR GLOBAL AUTHENTICATION GO TO REST_FRAMEWORK IN SETTING FILE AND UNCOMMENT IT


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # FOR LOCAL DEFIND BASIC AUTHENTICATION
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
