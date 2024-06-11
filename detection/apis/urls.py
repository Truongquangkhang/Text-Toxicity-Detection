# myapp/urls.py

from django.urls import path
from .views import  ContentDetection, HealthCheckView

urlpatterns = [
    path('detect-content/', ContentDetection.as_view(), name='content-detection'),
    path('health/', HealthCheckView.as_view(), name='health-check'),
]
