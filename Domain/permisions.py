from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_owner)
    
    
        
class IsAdvisor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_advisor)

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsOwnerOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    request. user and request.user.is_owner
                    )

class IsAdvisorOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    request. user and request.user.is_advisor
                    )

class IsStaffOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    request. user and request.user.is_staff
                    )


class IsObjOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and
            request.user.is_superuser or
            obj.user == request.user
        )

