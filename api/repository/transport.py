from api.models import UserTransportModel
from api.serializers import UserTransportMultisetSerializer


def transport_multiset(transports: UserTransportMultisetSerializer):
    old_transports = UserTransportModel.objects.filter(user_id=transports.data['user'])
    new_transports = []

    for transport in transports.data['transports']:
        (new_transport, _) = UserTransportModel.objects.get_or_create(
            pk=transport['id'],
            user_id=transports.data['user'],
            registration_number=transport['registration_number'],
            type_id=transport['type'],
            info=transport['info'])
        new_transports = [*new_transports, new_transport]

    transport_numbers = list(map(lambda x: x.registration_number, new_transports))
    for transport in old_transports:
        if transport.registration_number not in transport_numbers:
            transport.delete()

    return new_transports
