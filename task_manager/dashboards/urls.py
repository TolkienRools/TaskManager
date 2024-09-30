from django.urls import path

from .views import (
    ListDashboardView,
)

app_name = "dashboards"
urlpatterns = [
    path("dashboard/list/", ListDashboardView.as_view(), name="dashboard-list"),
]