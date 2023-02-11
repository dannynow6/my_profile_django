from django.shortcuts import render
from .models import MyLinks 
from .models import Project 


def index(request):
    """the home page for my portfolio app"""
    links = MyLinks.objects.all() 
    context = {"links": links}
    return render(request, "portfolio/index.html", context)


