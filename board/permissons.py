from rest_framework import permissions


class IsOwnerOrAdminReadOnly(permissions.BasePermission):
    """
    Разрешение на удаление и исправление админам
    или авторам статей или комментариев
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_staff
