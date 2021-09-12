from rest_framework.serializers import ModelSerializer

from api.models import OrderModel, ItemModel, OrderHistoryModel


class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'


class OrderHistorySerializer(ModelSerializer):
    class Meta:
        model = OrderHistoryModel
        fields = '__all__'
