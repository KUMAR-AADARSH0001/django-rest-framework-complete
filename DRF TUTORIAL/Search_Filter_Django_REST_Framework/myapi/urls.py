from django.urls import path
from . import views


urlpatterns = [
    path('all_student/', views.Studentlist.as_view()),
]
