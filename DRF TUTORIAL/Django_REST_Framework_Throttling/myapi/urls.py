from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# Creting Router
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi/', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]
