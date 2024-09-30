from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import TaskManagerUser

class TaskManagerUserAdmin(UserAdmin):
    pass


admin.site.register(TaskManagerUser, TaskManagerUserAdmin)
