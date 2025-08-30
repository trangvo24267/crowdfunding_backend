from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #confirming if HTTP verbs are safe to use
        # built-in function "SAFE_METHODS" with list of options - what am I allowed to use.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user
    
        