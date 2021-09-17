from django.contrib.auth.backends import UserModel
from django.db.models import Model, ForeignKey, CASCADE, TextField, BooleanField, IntegerField, CheckConstraint, Q, \
    ManyToManyField, F, Sum, AutoField

from api.models.user import UserTransportModel, PhoneModel, AddressModel, BuildModel


class OrderModel(Model):
    client = ForeignKey(UserModel, on_delete=CASCADE)
    actual_phone = ForeignKey(PhoneModel, on_delete=CASCADE)
    actual_address = ForeignKey(AddressModel, on_delete=CASCADE)

    class Meta:
        ordering = ['-id']


class OrderItemModel(Model):
    take_counter = IntegerField(default=0)
    item = ForeignKey('ItemModel', on_delete=CASCADE, null=True, related_name='order_item')
    order = ForeignKey('OrderModel', on_delete=CASCADE, null=True, related_name='order_item')


class ItemModel(Model):
    order = ManyToManyField(to=OrderModel, through=OrderItemModel, related_name='items')
    item = TextField()
    counter = IntegerField(default=0)
    code = TextField(unique=True, null=True)
    is_fragile = BooleanField(default=False)
    is_sunlight_damaged = BooleanField(default=False)
    is_moisture_damaged = BooleanField(default=False)
    is_temperature_damaged = BooleanField(default=False)
    min_temperature = IntegerField(null=True)
    max_temperature = IntegerField(null=True)

    class Meta:
        ordering = ['-id']


class OrderStatusModel(Model):
    status = TextField()


class OrderHistoryModel(Model):
    order = ForeignKey(OrderModel, on_delete=CASCADE)
    build = ForeignKey(BuildModel, on_delete=CASCADE, null=True)
    carrier = ForeignKey(UserModel, on_delete=CASCADE, null=True)
    transport = ForeignKey(UserTransportModel, on_delete=CASCADE, null=True)
    status = ForeignKey(OrderStatusModel, on_delete=CASCADE, default=OrderStatusModel.objects.get(status='initial').id)
    queue = IntegerField(default=0)

    class Meta:
        ordering = ['id', 'queue']
