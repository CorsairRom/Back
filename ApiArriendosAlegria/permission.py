from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Allows access only to SuperUser users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    
class IsStaffUser(BasePermission):
    """
    Allows access only to Staff users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)