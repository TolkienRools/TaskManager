from django.views.generic import (CreateView,
                                  UpdateView,
                                  ListView)

from tasks.models import Task

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from tasklists.models import TaskList
# from dashboards.models import Dashboard
from .forms import TaskListForm
from .mixins import DashboardMixin


class ListTaskView(ListView):
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


class CreateTaskListView(CreateView):
    model = TaskList
    form_class = TaskListForm
    template_name = 'tasklists/tasklist_form.html'  # Укажите ваш шаблон
    success_url = reverse_lazy('dashboards:dashboard-list')  # Укажите URL для перенаправления после успешного создания

    # def form_valid(self, form):
    #     # dashboard_id = self.kwargs.get('dashboard_id')
    #     #
    #     # dashboard = get_object_or_404(Dashboard, id=dashboard_id)
    #     #
    #     # tasklist = form.save(commit=False)
    #     # tasklist.dashboard = dashboard
    #     tasklist.save()
    #
    #     return super().form_valid(form)


# class UpdateTaskListView(DashboardMixin, UpdateView):
#     model = TaskList
#     form_class = TaskListForm
#     template_name = 'tasklists/tasklist_form.html'  # Укажите ваш шаблон
#     success_url = reverse_lazy('dashboard-list')  # Укажите URL для перенаправления после успешного обновления
#
#     def get_object(self, queryset=None):
#         # Получаем объект TaskList по идентификатору
#         tasklist_id = self.kwargs.get('pk')
#         return get_object_or_404(TaskList, id=tasklist_id)