from django.contrib.auth.backends import UserModel
from django.db.models import Model, ForeignKey, CASCADE, TextField, CharField, IntegerField, BooleanField


class RoleModel(Model):
    role = TextField(unique=True)


class UserRoleModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE)
    role = ForeignKey(RoleModel, on_delete=CASCADE)


class BuildModel(Model):
    type = TextField(unique=True)


class AddressModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE, null=True)
    address = TextField()
    type = ForeignKey(BuildModel, on_delete=CASCADE)
    is_actual = BooleanField(default=True)


class PhoneModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE)
    phone = CharField(max_length=20)


class TransportTypeModel(Model):
    type = TextField()


class UserTransportModel(Model):
    user = ForeignKey(UserModel, on_delete=CASCADE)
    type = ForeignKey(TransportTypeModel, on_delete=CASCADE)
    registration_number = TextField()
    info = TextField()

