from django.db import models

# Porfolio App Models


class Project(models.Model):
    """A model representing projects within my portfolio"""

    git_repo = models.URLField(max_length=300, blank=True)
    title = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    created_with = models.CharField(max_length=400)
    description = models.CharField(max_length=400)

    def __str__(self) -> str:
        """return a string representation of Project model"""
        title = self.title.title()
        repo = self.git_repo
        return f"{title} | {repo}"


class Profile(models.Model):
    """a model representing my resume profile"""

    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self) -> str:
        """return a string representation of Profile model"""
        profile_name = self.name.title()
        text = self.text
        return f"{profile_name} | {text[:50]}..."


class MyLinks(models.Model):
    """a model representing my resume important links"""

    name = models.CharField(max_length=125)
    url = models.URLField(max_length=300)

    class Meta:
        verbose_name_plural = "mylinks"

    def __str__(self) -> str:
        """return a string representation of MyLinks"""
        name = self.name.title()
        url = self.url
        return f"{name} | {url}"
