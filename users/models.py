
from django.contrib.auth import get_user_model
from django.db import models


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        indexes = [
            models.Index(fields=['user', 'created_at']),
        ]
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'
