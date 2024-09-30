import django_tables2 as tables
from django.urls import reverse
from tasklists.models import TaskList
from django.utils.safestring import mark_safe

class TaskListTable(tables.Table):
    name = tables.Column(accessor='name', verbose_name='Task Name')

    def render_name(self, value, record):
        # Создаем ссылку на обновление задачи
        url = reverse('tasklists:tasklist-list', args=[record.id])
        return mark_safe(f'<a href="{url}">{value}</a>')

    class Meta:
        model = TaskList
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name")
        attrs = {"class": "table"}
        sequence = ("id", "name")
