# myapp/urls.py

from django.urls import path
from .views import  ContentDetection

urlpatterns = [
    path('detect-content/', ContentDetection.as_view(), name='content-detection'),
]
