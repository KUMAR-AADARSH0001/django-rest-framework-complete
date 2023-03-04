from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# FOR GLOBAL AUTHENTICATION GO TO REST_FRAMEWORK IN SETTING FILE AND UNCOMMENT IT


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # FOR LOCAL DEFIND BASIC AUTHENTICATION
    authentication_classes = [BasicAuthentication]
    "if want to give permission to use authenticate member to use this"
    # permission_classes = [IsAuthenticated]
    "if want to give permission to use all member without authentication so give allowany"
    # permission_classes = [AllowAny]
    "only who can use this there's is staff==True and admin also"
    permission_classes = [IsAdminUser]
