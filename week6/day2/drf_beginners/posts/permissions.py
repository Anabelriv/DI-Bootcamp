from rest_framework import permissions


class ISAuthenticatedAndAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "POST"]:
            return request.user.is_authenticated

        elif request.method in ["PUT", "DELETE"]:
            if request.user.is_authenticated:
                return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "DELTE"]:
            return (
                obj.author == request.user
            )  # check if the current user is the author of the post

        return super().has_permission(request, view, obj)
