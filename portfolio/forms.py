from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    """
    A Form for adding new Projects
    """

    class Meta:
        model = Project
        fields = [
            "git_repo",
            "title",
            "created_with",
            "description",
        ]
        labels = {
            "git_repo": "Github Repo",
            "title": "Title",
            "created_with": "Created Using",
            "description": "Description",
        }
