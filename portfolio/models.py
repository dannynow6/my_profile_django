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


