from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import RoleModel, UserRoleModel, BuildModel, AddressModel, PhoneModel, TransportTypeModel, \
    UserTransportModel
from api.serializers.user import UserSerializer, RoleSerializer, UserRoleSerializer, BuildSerializer, AddressSerializer, \
    PhoneSerializer, TransportTypeSerializer, UserTransportSerializer


class UserViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = UserRoleModel.objects.all()
    serializer_class = UserRoleSerializer


class BuildViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = BuildModel.objects.all()
    serializer_class = BuildSerializer


class AddressViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer


class PhoneViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneSerializer


class TransportTypeViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = TransportTypeModel.objects.all()
    serializer_class = TransportTypeSerializer


class UserTransportViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = UserTransportModel.objects.all()
    serializer_class = UserTransportSerializer
