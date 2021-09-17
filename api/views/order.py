from django.db.transaction import atomic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from api.models import OrderModel, ItemModel, OrderHistoryModel, OrderItemModel, OrderStatusModel
from api.serializers import OrderSerializer, ItemSerializer, OrderHistorySerializer, OrderCreateSerializer, \
    OrderFullSerializer, OrderPartialSerializer, OrderHistoryCreateSerializer, StatusSerializer


class OrderViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderPartialSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        if self.action == 'retrieve':
            return OrderFullSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        items = request.data['items']
        with atomic():
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            OrderHistoryModel.objects.create(order_id=serializer.data['id'], status=OrderStatusModel.objects.get(status='initial'))
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderHistoryCreateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        if OrderHistoryModel.objects.filter(order_id=request.data['order'], status__status='ready').count():
            raise ValidationError('Already finished')
        request.data['queue'] = OrderHistoryModel.objects.filter(order_id=request.data['order']).count()
        self.request.data['queue'] = OrderHistoryModel.objects.filter(order_id=request.data['order']).count()
        return super(OrderHistoryViewSet, self).create(request, *args, **kwargs)


class OrderStatusViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = OrderStatusModel.objects.all()
    serializer_class = StatusSerializer
