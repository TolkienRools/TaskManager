from django.urls import path

from .views import (
    ListTaskView,
    CreateTaskListView,
)

app_name = "tasklists"

urlpatterns = [
    path('taskslist/list/<int:task_list_id>/', ListTaskView.as_view(), name='list-tasks'),
    path('taskslist/create/', CreateTaskListView.as_view(), name='tasklist-create'),
]