from django.urls import path
from . import views

urlpatterns = [
    path('all_student/', views.Student_LC.as_view()),
    path('student/<int:pk>/', views.Student_RUD.as_view()),

]
