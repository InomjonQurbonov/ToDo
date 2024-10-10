from rest_framework.permissions import BasePermission


class OnlyUserPermissions(BasePermission):
    """
        Здесь только пользователь может редактировать или удалять внесенные им изменения.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.user == request.user

        return False