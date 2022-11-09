"""
URL Configuration

https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v4/", include("api.urls")),
]
