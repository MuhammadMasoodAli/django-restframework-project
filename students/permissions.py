from rest_framework import permissions


# 1. Admin
class IsAdmin(permissions.BasePermission):
    # full access
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == 'admin'


# 2. Teacher
class IsTeacher(permissions.BasePermission):
    #   read, create, update access
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        role = request.user.profile.role
        if role != 'teacher':
            return False
        # not DELETE
        return request.method in ['GET', 'POST', 'PUT', 'PATCH']


# 3. Student
class IsStudent(permissions.BasePermission):
    # read only access
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        role = request.user.profile.role
        if role != 'student':
            return False

        return request.method == 'GET'
