from rest_framework.routers import DefaultRouter
from apps.users import views

router = DefaultRouter()
router.register('signup', views.UserRegisterAPIView, basename='signup')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls
