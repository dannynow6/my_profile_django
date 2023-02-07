from django.db import models

# Models representing education and work history from resume


class WorkExperience(models.Model):
    """A model representing my work experience from resume"""

    position_title = models.CharField(max_length=225)
    company_name = models.CharField(max_length=300)
    company_location = models.CharField(max_length=250)
    dates_employed = models.CharField(max_length=250)
    job_description = models.CharField(max_length=350)
    additional_job_description = models.CharField(max_length=400, blank=True)

    def __str__(self) -> str:
        """return a string representation of WorkExperience"""
        position = self.position_title.title()
        company = self.company_name.title()
        dates = self.dates_employed
        return f"{position} | {company} | {dates}"


class OtherWorkExperience(models.Model):
    """A model representing other work experience from resume"""

    position_title = models.CharField(max_length=225)
    company_name = models.CharField(max_length=300)
    company_location = models.CharField(max_length=250)
    dates_employed = models.CharField(max_length=250)
    job_description = models.CharField(max_length=350)
    additional_job_description = models.CharField(max_length=400, blank=True)
    specialization = models.CharField(max_length=250, blank=True)
    special_info = models.CharField(max_length=250, blank=True)
    special_info_2 = models.CharField(max_length=250, blank=True)

    def __str__(self) -> str:
        """return a string representation of WorkExperience"""
        position = self.position_title.title()
        company = self.company_name.title()
        dates = self.dates_employed
        return f"{position} | {company} | {dates}"


class Education(models.Model):
    """A model representing education history"""

    school_name = models.CharField(max_length=225)
    degree = models.CharField(max_length=50)
    area_of_study = models.CharField(max_length=75)
    date_attended = models.CharField(max_length=50)
    school_location = models.CharField(max_length=100)
    accolade = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        """return a string representation of Education"""
        school = self.school_name.title()
        degree = self.degree
        attended = self.date_attended
        return f"{school}, Degree: {degree} | {attended}"


class Skill(models.Model):
    """a model representing skills acquired"""

    LEVEL_CHOICES = [
        ("AL", "Advanced"),
        ("FL", "Familiar"),
        ("OL", "Other"),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)

    def __str__(self) -> str:
        """return string representation of Skill"""
        skill = self.name.title()
        level = self.level
        return f"{skill} | Proficiency: {level}"


class SoftSkill(models.Model):
    """a model representing soft skills acquired"""

    PROFICIENCY_CHOICES = [
        ("HP", "High"),
        ("MP", "Medium"),
        ("LP", "Low"),
    ]

    name = models.CharField(max_length=125)
    proficiency = models.CharField(max_length=25, choices=PROFICIENCY_CHOICES)

    def __str__(self) -> str:
        """return a string representation of SoftSkill"""
        skill = self.name.title()
        proficiency = self.proficiency
        return f"{skill} | Proficiency: {proficiency}"


class Hobby(models.Model):
    """a model representing hobbies from resume"""

    name = models.CharField(max_length=150)
    dates_practiced = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    url = models.URLField(blank=True, max_length=225)

    class Meta:
        verbose_name_plural = "hobbies"

    def __str__(self) -> str:
        """return a string representing Hobby model"""
        hobby = self.name.title()
        dates = self.dates_practiced
        description = self.description
        return f"{hobby} | {description} | {dates}"
