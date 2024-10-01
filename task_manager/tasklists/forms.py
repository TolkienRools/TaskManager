from django import forms
from tasklists.models import TaskList



class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name']

    def save(self, commit=True, user=None):
        task_list = super().save(commit=False)
        if user is not None:
            task_list.author = user
        if commit:
            task_list.save()
        return task_list
