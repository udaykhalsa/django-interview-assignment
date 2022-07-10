from rest_framework import permissions

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'librarian':
            return True
        return False

    
class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'member':
            return True
        return False