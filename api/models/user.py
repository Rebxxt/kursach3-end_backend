from django.contrib.auth.backends import UserModel
from django.db.models import Model, ForeignKey, CASCADE, TextField, CharField, IntegerField, BooleanField


class RoleModel(Model):
    role = TextField(unique=True)
    is_base = BooleanField(default=False)


class UserRoleModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE, related_name='roles')
    role = ForeignKey(RoleModel, on_delete=CASCADE)


class BuildModel(Model):
    type = TextField(unique=True)
    is_base = BooleanField(default=False)


class AddressModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE, null=True, related_name='addresses')
    address = TextField()
    type = ForeignKey(BuildModel, on_delete=CASCADE)
    is_actual = BooleanField(default=True)


class PhoneModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE, related_name='phones')
    phone = CharField(max_length=20)


class TransportTypeModel(Model):
    type = TextField(unique=True)
    is_base = BooleanField(default=False)


class UserTransportModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE, related_name='transports')
    type = ForeignKey(TransportTypeModel, on_delete=CASCADE)
    registration_number = TextField(unique=True)
    info = TextField()

