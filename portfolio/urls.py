"""Defines URL patterns for portfolio"""
from django.urls import path 
from . import views 

app_name = "portfolio" 
urlpatterns = [
    # Home page 
    path("", views.index, name="index"), 
    # A page for viewing featured projects 
    path("projects/", views.projects, name="projects"), 
    # A path to generate a pdf of project 
    path("<int:project_id>/print/", views.print_project, name="print_project"), 
    # A page to view a single project 
    path("<int:project_id>/", views.project, name="project"), 
]