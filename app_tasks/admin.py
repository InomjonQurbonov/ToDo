from django.contrib import admin
from app_tasks.models import Tasks


class AdminTasks(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'due_date')
    list_filter = ('status', 'due_date', 'user')
    search_fields = ('title', 'description', 'status', 'due_date', 'created_at', 'updated_at', 'user')


admin.site.register(Tasks, AdminTasks)
