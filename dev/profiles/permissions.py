# Extend to create base class for custom permission class
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Allows user to view all profiles but edit only their profile."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.id
