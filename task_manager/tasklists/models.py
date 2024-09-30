from readline import set_startup_hook

from django.db import models
# from dashboards.models import Dashboard

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=50, null=False)
    # dashboard = models.ForeignKey(Dashboard,
    #                               on_delete=models.CASCADE,
    #                               related_name="dashboard",
    #                               null=True)

    @property
    def total_tasks(self):
        from tasks.models import Task
        return Task.objects.filter(task_list_id=self).count()

    @property
    def completed_tasks(self):
        from tasks.models import Task
        return Task.objects.filter(task_list_id=self,
                                   status='completed').count()

    @property
    def completion_percentage(self):
        return round(self.completed_tasks / self.total_tasks * 100) if self.completed_tasks else 0


    def __str__(self):
        return self.name
