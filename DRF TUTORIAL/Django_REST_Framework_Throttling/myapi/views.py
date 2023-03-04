from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
"from .throttling import MyUserRateThrottle"  # it can user my own defined class


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # FOR LOCAL DEFIND BASIC AUTHENTICATION
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    "this can inharit MyUserRateThrottling from throtling.py file "
    # throttle_classes = [AnonRateThrottle, MyUserRateThrottle]
