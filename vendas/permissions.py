from rest_framework import permissions

class NotDeleteCategoria(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return False
        return True