from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from api.models import RoleModel, BuildModel, AddressModel, PhoneModel, TransportTypeModel, UserTransportModel, \
    UserRoleModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoleSerializer(ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'


class UserRoleSerializer(ModelSerializer):
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
