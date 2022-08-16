from rest_framework import permissions


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

# feed 글 관련 
# def has_object_permission(self, request, view, obj):

#     # 수정, 삭제
#     return obj.author == request.user

class IsAuthorOrReadonly(permissions.BasePermission):
    # 인증된 유저만 글을 읽을 수 있음
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # 작성자만 수정, 삭제 가능
    def has_object_permission(self, request, views, obj):
        # 조회 일 경우만 true
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.member_id == request.user