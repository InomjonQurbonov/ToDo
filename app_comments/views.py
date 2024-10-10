from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app_comments.models import Comment
from app_comments.serializers import CommentSerializer, GetCommentSerializers
from app_tasks.permissions import OnlyUserPermissions


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, OnlyUserPermissions]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetCommentSerializers
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
