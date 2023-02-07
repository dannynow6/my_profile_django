from django.contrib import admin

# Register your models here.
from .models import (
    WorkExperience,
    OtherWorkExperience,
    Education,
    Skill,
    SoftSkill,
    Hobby,
)

admin.site.register(WorkExperience)
admin.site.register(OtherWorkExperience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(SoftSkill)
admin.site.register(Hobby)
