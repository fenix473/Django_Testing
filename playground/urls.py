from django.urls import path, include
from . import views

# URL Configuration
urlpatterns = [
    path('hello/', views.say_hello),
]