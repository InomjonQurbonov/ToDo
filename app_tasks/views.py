from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app_tasks.models import Tasks
from app_tasks.serializers import TasksSerializer, GetTasksSerializers
from app_tasks.permissions import OnlyUserPermissions
from app_tasks.filters import TaskFilter


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    permission_classes = [IsAuthenticated, OnlyUserPermissions]
    filterset_class = TaskFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetTasksSerializers
        else:
            return TasksSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
