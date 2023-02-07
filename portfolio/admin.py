from django.contrib import admin

# Register your models here.
from .models import (
    Profile,
    Project,
    MyLinks,
)

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(MyLinks)
