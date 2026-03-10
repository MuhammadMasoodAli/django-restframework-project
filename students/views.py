from .models import Student
from .serializers import StudentSerializer
from .permissions import IsAdmin, IsTeacher, IsStudent
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RBACMixin:
    def get_permissions(self):
        user = self.request.user
        if not user.is_authenticated:
            return [IsAuthenticated()]
        if not hasattr(user, 'profile') or not user.profile.role:
            return [IsAuthenticated()]
        
        role = user.profile.role
        if role == 'admin':
            return [IsAdmin()]
        elif role == 'teacher':
            return [IsTeacher()]
        elif role == 'student':
            return [IsStudent()]
        return [IsAuthenticated()]


class StudentModelViewSet(RBACMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
