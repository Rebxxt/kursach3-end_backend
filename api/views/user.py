from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.serializers.user import UserSerializer


class UserViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
