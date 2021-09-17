from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from api.models import OrderModel, ItemModel, OrderHistoryModel, OrderItemModel, OrderStatusModel
from api.serializers import PhoneSerializer, AddressSerializer, BuildSerializer, UserSerializer, UserTransportSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['items']


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'


class OrderPartialSerializer(ModelSerializer):
    actual_phone = PhoneSerializer()
    actual_address = AddressSerializer()

    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['items']


class OrderFullSerializer(ModelSerializer):
    id = IntegerField()
    actual_phone = PhoneSerializer()
    actual_address = AddressSerializer()
    items = ItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['items']


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


class StatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatusModel
        fields = '__all__'


class OrderHistorySerializer(ModelSerializer):
    queue = IntegerField(allow_null=True)
    build = BuildSerializer(allow_null=True)
    carrier = UserSerializer(allow_null=True)
    transport = UserTransportSerializer(allow_null=True)
    status = StatusSerializer(allow_null=True)
    order = OrderPartialSerializer(allow_null=True)

    class Meta:
        model = OrderHistoryModel
        fields = '__all__'


class OrderHistoryCreateSerializer(ModelSerializer):
    queue = IntegerField(allow_null=True)

    class Meta:
        model = OrderHistoryModel
        fields = '__all__'
