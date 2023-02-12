from django.shortcuts import render
from .models import MyLinks
from .models import Project
import datetime

# Imports for using ReportLab for PDF gen
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet


def index(request):
    """the home page for my portfolio app"""
    links = MyLinks.objects.all()
    context = {"links": links}
    return render(request, "portfolio/index.html", context)


def projects(request):
    """A page for viewing current featured projects"""
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "portfolio/projects.html", context)


def print_project(request, project_id):
    # Need to add a view for viewing projects - view all in list with view/print options
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    project = Project.objects.get(id=project_id)
    repo = project.git_repo
    title = project.title
    date = project.date_added  # use .strftime('%m/%d/%Y')
    created_with = project.created_with
    description = project.description
    project_id = project.id

    logo = "./static/img/dg.jpg"
    p.drawImage(logo, 216, 576, width=None, height=None)

    title_obj = p.beginText(270, 504)
    title_obj.setFont("Helvetica-Oblique", 14, leading=None)
    title_obj.textLine(text=f"{title.title()}")
    p.drawText(title_obj)

    date_obj = p.beginText(504, 468)
    date_obj.setFont("Helvetica", 11, leading=None)
    date_obj.textLine(text=f"{date.strftime('%m/%d/%Y')}")
    p.drawText(date_obj)

    create_obj = p.beginText(54, 400)
    create_obj.setFont("Helvetica", 10, leading=None)
    create_obj.textLine(text=f"Created using: {created_with}")
    p.drawText(create_obj)

    des_obj = p.beginText(54, 328)
    des_obj.setFont("Helvetica", 11, leading=None)
    des_obj.textLine(text=f"{description[:100]}")
    p.drawText(des_obj)
    
    des2_obj = p.beginText(72, 310)
    des2_obj.setFont("Helvetica", 11, leading=None) 
    des2_obj.textLine(text=f"{description[100:]}")
    p.drawText(des2_obj)

    repo_obj = p.beginText(72, 256)
    repo_obj.setFont("Helvetica", 11, leading=None)
    repo_obj.textLine(text=f"{repo}")
    p.drawText(repo_obj)

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"project{project_id}.pdf")


def project(request, project_id):
    """a page for viewing the details of a single project"""
    project = Project.objects.get(id=project_id)
    if project.title.lower() == "photo blog":
        url = "https://github.com/dannynow6/dg-photo"
    elif project.title.lower() == "adventure game":
        url = "https://github.com/dannynow6/adventure-game-v2" 
    elif project.title.lower() == "podcast app":
        url = "https://github.com/dannynow6/esp-kivy-project" 
    context = {"project": project, "url": url}
    return render(request, "portfolio/project.html", context)
