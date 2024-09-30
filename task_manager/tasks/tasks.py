from celery import shared_task
import datetime
from .models import Task


@shared_task
def my_hourly_task():
    print(f"Task executed at {datetime.datetime.now()}")