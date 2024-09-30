#!/bin/sh

until cd /app/task_manager
do
    echo "Waiting for server volume..."
done

# run celery beat :)
celery -A task_manager beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler