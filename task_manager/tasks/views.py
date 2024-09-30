from django.views.generic import (CreateView,
                                  UpdateView)
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from tasklists.models import TaskList
from .models import Task
from .forms import TaskCreateUpdateForm


class CreateTaskView(CreateView):
    form_class = TaskCreateUpdateForm
    template_name = 'tasks/task_form.html'

    def get_initial(self):
        initial = super().get_initial()
        # Установите значение task_list_id по умолчанию
        initial['task_list_id'] = self.kwargs['task_list_id']
        return initial

    def get_success_url(self):
        # Get the task_list_id from the URL kwargs
        task_list_id = self.kwargs['task_list_id']
        # Construct the success URL using the task_list_id
        return reverse_lazy('tasklists:list-tasks', kwargs={'task_list_id': task_list_id})


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskCreateUpdateForm
    # success_url = reverse_lazy('dashboards:dashboard-list')

    def form_valid(self, form):
        # Сохраните задачу
        task = form.save()

        # Перенаправьте на нужный URL
        return redirect(reverse('tasklists:list-tasks',
                                kwargs={'task_list_id': task.task_list_id.id}))

    # def get_success_url(self):
    #     # Get the task_list_id from the URL kwargs
    #     task_list_id = self.kwargs['task_list_id']
    #     # Construct the success URL using the task_list_id
    #     return reverse_lazy('tasklists:list-tasks', kwargs={'task_list_id': task_list_id})
