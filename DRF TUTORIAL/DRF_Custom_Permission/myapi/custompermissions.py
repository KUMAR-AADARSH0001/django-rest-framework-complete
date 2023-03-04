from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        "if you loged in then agin it will call you have not permission to post data"
        # if request.method == 'POST':
        #     return True
        return False
