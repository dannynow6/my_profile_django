from django.shortcuts import render


def index(request):
    """the home page for my portfolio app"""
    return render(request, "portfolio/index.html")
