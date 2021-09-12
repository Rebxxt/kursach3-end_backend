from django.contrib.auth.backends import UserModel
from django.db.models import Model, ForeignKey, CASCADE, TextField, BooleanField, IntegerField, CheckConstraint, Q

from api.models.user import UserTransportModel, PhoneModel


class OrderModel(Model):
    client = ForeignKey(UserModel, on_delete=CASCADE)
    actual_phone = ForeignKey(PhoneModel, on_delete=CASCADE)
    actual_address = ForeignKey()


class ItemModel(Model):
    order = ForeignKey(OrderModel, on_delete=CASCADE)
    item = TextField()
    is_fragile = BooleanField(default=False)
    is_sunlight_damaged = BooleanField(default=False)
    is_moisture_damaged = BooleanField(default=False)
    is_temperature_damaged = BooleanField(default=False)
    min_temperature = IntegerField(null=True)
    max_temperature = IntegerField(null=True)


class OrderHistoryModel(Model):
    order = ForeignKey(OrderModel, on_delete=CASCADE)
    carrier = ForeignKey(UserModel, on_delete=CASCADE)
    transport = ForeignKey(UserTransportModel, on_delete=CASCADE)