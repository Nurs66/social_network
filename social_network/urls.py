from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.posts.views import AnalyticAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Social network",
        default_version='v1',
        description="API for Social network",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('users/', include('apps.users.urls')),
    path('posts/', include('apps.posts.urls')),
    path('analitics/', AnalyticAPIView.as_view(), name='analitics'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
    path('auth/', include('rest_framework.urls')),

    # auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

