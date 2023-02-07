"""Defines URL patterns for portfolio"""
from django.urls import path 
from . import views 

app_name = "portfolio" 
urlpatterns = [
    # Home page 
    path("", views.index, name="index"), 
]