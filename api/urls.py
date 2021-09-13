from rest_framework import routers

from api.views.order import OrderViewSet, ItemViewSet, OrderHistoryViewSet
from api.views.user import UserViewSet, RoleViewSet, UserRoleViewSet, BuildViewSet, AddressViewSet, PhoneViewSet, \
    TransportTypeViewSet, UserTransportViewSet, AuthViewSet

temp = routers.SimpleRouter()
temp.register(r'user', UserViewSet)
temp.register(r'auth', AuthViewSet)
temp.register(r'role', RoleViewSet)
temp.register(r'user-role', UserRoleViewSet)
temp.register(r'build', BuildViewSet)
temp.register(r'address', AddressViewSet)
temp.register(r'phone', PhoneViewSet)
temp.register(r'transport-type', TransportTypeViewSet)
temp.register(r'user-transport', UserTransportViewSet)
temp.register(r'order', OrderViewSet)
temp.register(r'item', ItemViewSet)
temp.register(r'order-history', OrderHistoryViewSet)

urlpatterns = temp.urls
