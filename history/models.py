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
