from django.views.generic import (CreateView,
                                  ListView)

from tasks.models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TaskList
from .forms import TaskListForm


class ListTaskView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Task

    template_name = 'tasklists/tasklist.html'  # Укажите ваш шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # # Получаем идентификатор списка задач из URL
        task_list_id = self.kwargs.get('task_list_id')

        # Получаем список задач по идентификатору
        tasklist = TaskList.objects.get(id=task_list_id)
        tasks = Task.objects.filter(task_list_id=tasklist)

        # Инициализируем переменные для аналитики
        completed_tasks = tasks.filter(status='completed').count()
        in_progress_tasks = tasks.filter(status='in_progress').count()
        not_started_tasks = tasks.filter(status='pending').count()

        # Добавляем данные в контекст
        context['tasks'] = tasks
        context['completed_tasks'] = completed_tasks
        context['in_progress_tasks'] = in_progress_tasks
        context['not_started_tasks'] = not_started_tasks
        context['task_list_id'] = task_list_id

        return context


class CreateTaskListView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = TaskList
    form_class = TaskListForm
    template_name = 'tasklists/tasklist_form.html'  # Укажите ваш шаблон
    success_url = reverse_lazy('dashboards:dashboard-list')  # Укажите URL для перенаправления после успешного создания

    def form_valid(self, form):
        form.save(user=self.request.user)
        return super().form_valid(form)

