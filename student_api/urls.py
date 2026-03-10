from django.contrib import admin
from students.views import StudentModelViewSet

# Default Router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# JWT
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Student API",
        default_version='v1',
        description="DRF Beginner Friendly API Project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('students', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Login/Logout on  django dashboard
    path('auth/', include('rest_framework.urls')),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
