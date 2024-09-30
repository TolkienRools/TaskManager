from django import forms
from tasklists.models import TaskList



class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name']