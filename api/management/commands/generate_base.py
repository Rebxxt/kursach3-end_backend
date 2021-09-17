from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from api.models import RoleModel, UserRoleModel, BuildModel, TransportTypeModel, OrderStatusModel


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # roles
        base_roles = ['user', 'admin', 'worker', 'carrier', 'manager']
        roles = []
        for role in base_roles:
            roles.append(RoleModel.objects.create(role=role, is_base=True))

        # admin
        password = 'pbkdf2_sha256$260000$cHPXbd3VFJ5A73AQyZA92T$SGPRXowzNKXL9EviLYSEGegYO4YyHwfkERC+yK1uGPY='
        user_admin = get_user_model().objects.create(username='admin',
                                                     password=password,
                                                     is_superuser=True)
        for role in roles:
            UserRoleModel.objects.create(role=role, user=user_admin)

        # builds
        base_builds = ['home', 'office', 'storage']
        for build in base_builds:
            BuildModel.objects.create(is_base=True, type=build)

        # transport types
        base_transport_types = ['car', 'truck', 'air', 'cargo']
        for transport_types in base_transport_types:
            TransportTypeModel.objects.create(is_base=True, type=transport_types)

        # order history statuses
        statuses = ['ready', 'finish_point', 'delivery', 'sort', 'initial']
        for status in statuses:
            OrderStatusModel.objects.create(status=status)

        self.stdout.write(self.style.SUCCESS('Successfully generate base'))
