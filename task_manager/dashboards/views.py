from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  UpdateView,
                                  ListView)

from tasklists.models import TaskList
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class ListDashboardView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = TaskList
    template_name = 'dashboards/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_tasks = 0
        total_completed = 0
        in_progress_tasks = 0
        not_started_tasks = 0

        tasklists = TaskList.objects.filter(author=self.request.user).all()

        for tasklist in tasklists:
            tasks = Task.objects.filter(task_list_id=tasklist.id)
            total_tasks += tasks.count()
            completed = tasks.filter(status='completed').count()
            total_completed += completed
            in_progress_tasks += tasks.filter(status='in_progress').count()
            not_started_tasks += tasks.filter(status='pending').count()

        overall_completion_percentage = round(total_completed / total_tasks * 100) if total_tasks > 0 else 0
        completed_percentage = round(total_completed / total_tasks * 100) if total_tasks > 0 else 0
        in_progress_percentage = round(in_progress_tasks / total_tasks * 100) if total_tasks > 0 else 0
        not_started_percentage = round(not_started_tasks / total_tasks * 100) if total_tasks > 0 else 0

        context['tasklists'] = tasklists
        context['total_tasks'] = total_tasks
        context['total_completed'] = total_completed
        context['overall_completion_percentage'] = overall_completion_percentage
        context['completed_percentage'] = completed_percentage
        context['in_progress_percentage'] = in_progress_percentage
        context['not_started_percentage'] = not_started_percentage
        context['in_progress_tasks'] = in_progress_tasks
        context['not_started_tasks'] = not_started_tasks

        return context
