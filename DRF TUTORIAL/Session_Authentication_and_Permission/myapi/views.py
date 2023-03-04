from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# FOR GLOBAL AUTHENTICATION GO TO REST_FRAMEWORK IN SETTING FILE AND UNCOMMENT IT


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # FOR LOCAL DEFIND BASIC AUTHENTICATION
    authentication_classes = [SessionAuthentication]
    "if want to give permission to use authenticate member to use this"
    # permission_classes = [IsAuthenticated]
    "if want to give permission to use all member without authentication so give allowany"
    # permission_classes = [AllowAny]
    "only who can use this there's is staff==True and admin also"
    # permission_classes = [IsAdminUser]
    "It is use for Authenticate user perform any task and unauthenticate user only can read and watch"
    # permission_classes = [IsAuthenticatedOrReadOnly]
    "If you authenticate user It can give only read permission"
    "If you wat to give any permission then go to admin pannel - User permissions"
    # permission_classes = [DjangoModelPermissions]
    "This is similar to DjangoModelPermissions"
    "But it can give permission to unauthenticate user to read only"
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
