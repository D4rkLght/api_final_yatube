from rest_framework import permissions


class IsAuthorChangeOnly(permissions.BasePermission):
    """Изменение чужого контента запрещено."""

    def has_object_permission(self, request, view, obj):
        method = request.method in permissions.SAFE_METHODS
        return method or obj.author == request.user
