from django.urls import path

from . import services

urlpatterns = [
    path("api/auth/login", services.auth_login)
]