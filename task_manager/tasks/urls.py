from django.urls import path

from .views import (
    CreateTaskView,
    UpdateTaskView
)

app_name = "tasks"
urlpatterns = [
    path("task/create/<int:task_list_id>/", CreateTaskView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", UpdateTaskView.as_view(), name="task-update"),
]