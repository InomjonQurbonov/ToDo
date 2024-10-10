from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_tasks import views

router = DefaultRouter()

router.register('tasks', views.TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]