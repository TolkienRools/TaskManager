#!/bin/sh

until cd /app/task_manager
do
    echo "Waiting for server volume..."
done

celery -A task_manager purge

# run a worker :)
celery -A task_manager worker --loglevel=info --concurrency 1 -E