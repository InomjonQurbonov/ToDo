from rest_framework import serializers
from app_comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at',]


class GetCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'task', 'user']
