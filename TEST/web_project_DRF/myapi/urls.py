from django.urls import path
from myapi import views
from myapi.models import LogMessage


urlpatterns = [
    path("log_create/", views.homelistview),
    path('all_logs/', views.homelistview),
]
