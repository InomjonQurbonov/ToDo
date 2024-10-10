from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

TASKS_TYPES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]


class Tasks(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=TASKS_TYPES, default='pending')
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def clean(self):
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError('Дата выполнения задачи не может быть в прошлом.')

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'
