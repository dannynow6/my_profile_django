"""Defines URL patterns for History App - portfolio"""
from django.urls import path
from . import views

app_name = "history"
urlpatterns = [
    # A page for viewing education history details
    path("my_education/", views.my_education, name="my_education"),
    # A page for viewing work experience 
    path("work_experience/", views.work_experience, name="work_experience"), 
    # A page for viewing skills 
    path("skills/", views.skills, name="skills"), 
]
