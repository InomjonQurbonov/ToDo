from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_comments import views

router = DefaultRouter()

router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
