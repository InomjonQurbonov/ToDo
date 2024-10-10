from rest_framework import serializers
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class GetTasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status', 'due_date', 'created_at', 'updated_at']
