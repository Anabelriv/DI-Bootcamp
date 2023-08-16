from rest_framework.permissions import BasePermission


class IsForecaster(BasePermission):
    def has__object_permission(self, request, view, obj):
        if request.method == ["DELETE"]:
            return request.user == obj.forecaster
        if request.method in ["POST", "GET", "PUT"]:
            return True

        # elif request.method in ["PUT", "DELETE"]:
        #     if request.user.is_authenticated:
        #         return request.user.is_staff

    # def has_object_permission(self, request, view, obj):
    #     if request.method in ["PUT", "DELTE"]:
    #         return (
    #             obj.author == request.user
    #         )  # check if the current user is the author of the post

    #     return super().has_permission(request, view, obj)
