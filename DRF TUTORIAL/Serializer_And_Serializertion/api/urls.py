from django.urls import path
from api import views


urlpatterns = [
    path('stu_info/<int:pk>', views.student_detail),
    path('stu_info/list/', views.student_list),
]
