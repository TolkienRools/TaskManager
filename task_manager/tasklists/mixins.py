


class DashboardMixin:
    def form_valid(self, form):
        # Получаем идентификатор дашборда из URL
        dashboard_id = self.kwargs.get('dashboard_id')
        # Сохраняем объект TaskList с привязкой к дашборду
        tasklist = form.save(commit=False)
        tasklist.dashboard_id = dashboard_id  # Предполагается, что у вас есть связь с дашбордом
        tasklist.save()
        return super().form_valid(form)