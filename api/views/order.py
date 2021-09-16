from django.db.transaction import atomic
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from api.models import OrderModel, ItemModel, OrderHistoryModel, OrderItemModel
from api.serializers import OrderSerializer, ItemSerializer, OrderHistorySerializer, OrderCreateSerializer, \
    OrderFullSerializer


class OrderViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderFullSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        items = request.data['items']
        with atomic():
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

            for item in items:
                OrderItemModel.objects.create(item_id=item['id'],
                                              take_counter=item['counter'],
                                              order_id=response.data['id'])

        return response


class ItemViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class OrderHistoryViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = OrderHistoryModel.objects.all()
    serializer_class = OrderHistorySerializer
