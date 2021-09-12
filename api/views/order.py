from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import OrderModel, ItemModel, OrderHistoryModel
from api.serializers import OrderSerializer, ItemSerializer, OrderHistorySerializer


class OrderViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer


class ItemViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class OrderHistoryViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = OrderHistoryModel.objects.all()
    serializer_class = OrderHistorySerializer
