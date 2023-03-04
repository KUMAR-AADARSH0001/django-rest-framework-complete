from django.urls import path
from . import views

urlpatterns = [
    path('list_create/', views.StudentListCreate.as_view()),
    path('retrieve_update/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    path('retrieve_delete/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    path('retrieve_update_destroy/<int:pk>/',
         views.StudentRetrieveUpdateDestroy.as_view()),
]
