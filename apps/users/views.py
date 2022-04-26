from rest_framework import viewsets, mixins, permissions

from apps.users import serializers
from apps.users.models import User


class UserRegisterAPIView(viewsets.GenericViewSet,
                          mixins.CreateModelMixin,
                          ):
    queryset = User.objects.all()
    serializer_class = serializers.UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  ):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
