from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# Creting Router
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi/', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
