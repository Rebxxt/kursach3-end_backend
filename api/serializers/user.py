from django.contrib.auth.models import User
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from api.models import RoleModel, BuildModel, AddressModel, PhoneModel, TransportTypeModel, UserTransportModel, \
    UserRoleModel


class AuthSerializer(Serializer):
    login = CharField()
    password = CharField()


class RoleSerializer(ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'


class UserRoleSerializer(ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = UserRoleModel
        fields = '__all__'


class UserRoleUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserRoleModel
        fields = '__all__'


class BuildSerializer(ModelSerializer):
    class Meta:
        model = BuildModel
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = '__all__'


class TransportTypeSerializer(ModelSerializer):
    class Meta:
        model = TransportTypeModel
        fields = '__all__'


class UserTransportSerializer(ModelSerializer):
    class Meta:
        model = UserTransportModel
        fields = '__all__'


class UserSerializer(ModelSerializer):
    addresses = AddressSerializer(many=True)
    roles = UserRoleSerializer(many=True)
    phones = PhoneSerializer(many=True)
    transports = UserTransportSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserTransportMultisetSerializer(Serializer):
    transports = UserTransportSerializer(many=True)
    user = UserSerializer()
