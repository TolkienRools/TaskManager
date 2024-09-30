from django.db import models
from django.utils import timezone

from tasklists.models import TaskList

#
# class Tag(models.Model):
#     name = models.CharField(max_length=50, null=False)
#
#     def __str__(self):
#         return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    name = models.CharField(max_length=50, null=False)
    description = models.TextField(default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES,
                                default='low')
    create_date = models.DateField(null=False, default=timezone.now)
    deadline_date = models.DateField(null=True)
    task_list_id = models.ForeignKey(TaskList,
                                     on_delete=models.CASCADE,
                                     related_name="task_list",
                                     null=True)
    # tags = models.ManyToManyField(Tag, related_name="tasks")

    @property
    def days_remaining(self):
        return (self.deadline_date - timezone.now().date()).days

    @property
    def progress(self):
        return max(0, self.days_remaining)

class File(models.Model):
    name = models.CharField(max_length=50, null=False)
    storage_path = models.CharField(max_length=100, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name="files", null=True)

    # def __str__(self):
    #     return self.name
