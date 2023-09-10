from django.urls import path
from .views import home, register, login

urlpatterns = [
    path("", home),
    path('register', register),
    path('login', login),

]