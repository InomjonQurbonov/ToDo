from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo API system for users",
        default_version='v1',
        description="ToDo API System for Users is a RESTful API designed to manage tasks and to-do items for \n"
                    "registered users. This system allows users to create, update, delete, and retrieve tasks through "
                    "\n "
                    "standard HTTP requests.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="inomjonqurbonov916@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # token authentication urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger urls
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # apps urls
    path('tasks/', include('app_tasks.urls')),
    path('users/', include('users.urls')),
    path('comments/', include('app_comments.urls'),)
]
