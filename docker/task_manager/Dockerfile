FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip "poetry==1.8.3"
RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./

RUN poetry install

RUN poetry show

ADD ./task_manager /app/task_manager
ADD ./docker /app/docker

RUN chmod +x /app/docker/task_manager/server-entrypoint.sh
RUN chmod +x /app/docker/task_manager/worker-entrypoint.sh

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_manager.wsgi:application"]