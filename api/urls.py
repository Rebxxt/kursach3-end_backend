from rest_framework import routers

from api.views.user import UserViewSet

temp = routers.SimpleRouter()
temp.register(r'users', UserViewSet)

urlpatterns = temp.urls
