from django.contrib.auth import get_user_model
from django.db import models
from app_tasks.models import Tasks

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'
