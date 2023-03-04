from django.urls import path
from . import views


urlpatterns = [
    path('stu_api/',views.student_api),
]