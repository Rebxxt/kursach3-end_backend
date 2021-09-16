from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from api.models import OrderModel, ItemModel, OrderHistoryModel
from api.serializers import PhoneSerializer, AddressSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['items']


class OrderFullSerializer(ModelSerializer):
    actual_phone = PhoneSerializer()
    actual_address = AddressSerializer()

    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['items']


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'


class ItemShortSerializer(ModelSerializer):
    id = IntegerField()

    class Meta:
        model = ItemModel
        fields = ['id', 'counter']


class OrderCreateSerializer(ModelSerializer):
    items = ItemShortSerializer(many=True, allow_null=True)

    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderHistorySerializer(ModelSerializer):
    class Meta:
        model = OrderHistoryModel
        fields = '__all__'
