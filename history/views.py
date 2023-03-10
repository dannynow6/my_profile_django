from django.shortcuts import render
from .models import WorkExperience
from .models import OtherWorkExperience
from .models import Education
from .models import Skill
from .models import SoftSkill
from .models import Hobby
from portfolio.models import Profile
from portfolio.models import MyLinks 


# Views for History App of portfolio


def my_education(request):
    """A view for displaying Education information"""
    edu = Education.objects.all()
    context = {"edu": edu}
    return render(request, "history/my_education.html", context)


def work_experience(request):
    """a page for viewing work experience"""
    work = WorkExperience.objects.all()
    otherwork = OtherWorkExperience.objects.all()
    context = {"work": work, "otherwork": otherwork}
    return render(request, "history/work_experience.html", context)


def skills(request):
    """a page for viewing my skills"""
    skills = Skill.objects.all()
    soft_skills = SoftSkill.objects.all()
    context = {"skills": skills, "soft_skills": soft_skills}
    return render(request, "history/skills.html", context)


def about(request):
    """A view displaying about me info and hobby info"""
    hobbies = Hobby.objects.all()
    summary = Profile.objects.get(id=1)
    links = MyLinks.objects.all() 
    context = {"hobbies": hobbies, "summary": summary, "links": links}
    return render(request, "history/about.html", context)
