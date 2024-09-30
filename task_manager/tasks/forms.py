from django.forms import (ModelForm,
                          CheckboxSelectMultiple,
                          FileField,
                          ClearableFileInput)

from django import forms

from .models import Task


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class TaskCreateUpdateForm(ModelForm):
    # file_field = MultipleFileField()

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority',
                  'create_date', 'deadline_date',
                  'task_list_id',] # tags
        widgets = {
            'create_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(TaskCreateForm, self).__init__(*args, **kwargs)
    #
    #     # Customize the tags field to use CheckboxSelectMultiple
    #     # self.fields['tags'].widget = CheckboxSelectMultiple()
    #     # self.fields['tags'].queryset = Tag.objects.all()  # Get all Tag objects
    #
    #     # Add Bootstrap classes to all fields
    #     for name, field in self.fields.items():
    #         field.widget.attrs["class"] = "form-control col-md-6"

