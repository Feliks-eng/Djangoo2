from django import forms
from app.models import Task

class TaskInfo(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descriptions']