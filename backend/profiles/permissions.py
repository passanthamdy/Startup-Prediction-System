from rest_framework import permissions

class UserWritePermission(permissions.BasePermission):
    message = 'Editing or updating is restricted to the current user only.'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
