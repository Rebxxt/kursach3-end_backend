from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import RoleModel, UserRoleModel, BuildModel, AddressModel, PhoneModel, TransportTypeModel, \
    UserTransportModel
from api.repository.transport import transport_multiset
from api.serializers.user import UserSerializer, RoleSerializer, UserRoleSerializer, BuildSerializer, AddressSerializer, \
    PhoneSerializer, TransportTypeSerializer, UserTransportSerializer, AuthSerializer, UserRoleUpdateSerializer, \
    UserTransportMultisetSerializer


class AuthViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema()
    @action(methods=['GET'], detail=False)
    def current(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)

    @swagger_auto_schema(request_body=AuthSerializer)
    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        user = authenticate(username=request.data['login'], password=request.data['password'])
        login(request, user)
        return Response(self.serializer_class(user).data)

    @swagger_auto_schema()
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request, *args, **kwargs):
        logout(request)
        return Response()

    @swagger_auto_schema(request_body=AuthSerializer)
    @action(methods=['POST'], detail=False)
    def registration(self, request, *args, **kwargs):
        user = User.objects.create_user(username=request.data['login'], password=request.data['password'])
        user = authenticate(username=user.username, password=request.data['password'])
        login(request, user)
        return Response(self.serializer_class(user).data)


class UserViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'roles':
            return UserRoleSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = self.queryset
        if role := self.request.query_params.get('role'):
            queryset = queryset.filter(roles__role__role=role)

        return queryset

    @swagger_auto_schema()
    @action(methods=['GET'], detail=True)
    def roles(self, request, *args, **kwargs):
        roles = UserRoleModel.objects.filter(user_id=kwargs['pk'])
        return Response(self.get_serializer(roles, many=True).data)


class RoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = UserRoleModel.objects.all()
    serializer_class = UserRoleSerializer

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return UserRoleUpdateSerializer
        return self.serializer_class


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

    def get_serializer_class(self):
        if self.action == 'multiset':
            return UserTransportMultisetSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = self.queryset
        if user := self.request.query_params.get('user'):
            queryset = queryset.filter(user_id=user)
        return queryset

    @swagger_auto_schema(request_body=UserTransportMultisetSerializer)
    @action(methods=['PATCH'], detail=False)
    def multiset(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        transport_multiset(serializer)
        return Response()
