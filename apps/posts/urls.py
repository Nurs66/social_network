from rest_framework.routers import DefaultRouter

from apps.posts import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('likes', views.LikeViewSet, basename='likes')

urlpatterns = router.urls
