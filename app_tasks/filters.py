from django_filters import rest_framework as filters
from app_tasks.models import Tasks


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Tasks
        fields = ['status', 'due_date']
