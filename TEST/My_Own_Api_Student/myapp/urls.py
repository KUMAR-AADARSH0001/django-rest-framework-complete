from django.urls import path
from . import views


urlpatterns = [
    path('stu_list/', views.StudentList.as_view())
]
