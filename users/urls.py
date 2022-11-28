"""Defines URL patterns for registration"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
