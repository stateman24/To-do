from django import forms
from core.models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "user")

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "add-task",
            "class": "add-task",
            "placeholder": "Add your task here"
        }
    ))
