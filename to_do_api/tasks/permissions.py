from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_staff
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff