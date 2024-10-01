from celery import shared_task
from django.contrib.auth.models import User

from .utils import send_email
from .models import Task


@shared_task
def task_reminder_emails():

    users = User.objects.all()

    for user in users:
        if user.email:
            tasks = Task.objects.filter(task_list_id__author=user)
            for task in tasks:
                if task.days_remaining == 1:
                    send_email('Task deadline soon',
                               f'Your task {task.name} '
                               f'close to deadline', [user.email])
