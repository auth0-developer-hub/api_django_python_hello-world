from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):
    permission = None

    """
    User is allowed access if has the expected permission
    """
    def has_permission(self, request, view):
        return request.auth and self.permission in request.auth.get('permissions', [])

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class HasAdminPermission(HasPermission):
    permission = "read:admin-messages"
