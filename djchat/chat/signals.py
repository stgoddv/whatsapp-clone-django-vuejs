from friends.signals import (friendship_request_created,
                             friendship_request_canceled,
                             friendship_request_accepted
                             )
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Room

channel_layer = get_channel_layer()


@receiver(friendship_request_created)
def friendship_request_created_callback(sender, **kwargs):
    async_to_sync(channel_layer.group_send)(
        f"group_general_user_{sender.to_user.id}", {
            "type": "chat_message",
            "message": 'update_received',
            'data': {}
        })


@receiver(friendship_request_canceled)
def friendship_request_canceled_callback(sender, to_user, **kwargs):
    async_to_sync(channel_layer.group_send)(
        f"group_general_user_{to_user.id}", {
            "type": "chat_message",
            "message": 'update_received',
            'data': {}
        })


@receiver(friendship_request_accepted)
def friendship_request_accepted_callback(sender, to_user, from_user, **kwargs):
    room, _ = Room.objects.get_or_create(kind=1)
    room.participants.add(to_user.id, from_user.id)
    room.signal_to_room('update_rooms', data={})
    async_to_sync(channel_layer.group_send)(
        f"group_general_user_{from_user.id}", {
            "type": "chat_message",
            "message": 'update_sent',
            'data': {}
        })
