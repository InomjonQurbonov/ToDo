from django.contrib import admin
from app_comments.models import Comment


class AdminComment(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'task')
    list_filter = ('created_at', 'task', 'user')
    search_fields = ('text', 'created_ad', 'task', 'user')


admin.site.register(Comment, AdminComment)
