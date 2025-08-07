from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the author of a post/comment to edit or delete it.
    Everyone else can only read.
    """

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow update/delete if the user is the author or staff
        return obj.author == request.user or request.user.is_staff
