from django.db import models
from django.conf import settings

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import uuid

channel_layer = get_channel_layer()


class MessageManager(models.Manager):
    def get_pending_messages(self, user):
        pending_messages_qs = user.pending_messages.order_by('timestamp')
        for message in pending_messages_qs:
            message.remove_user_from_pending(user)
        return pending_messages_qs

    def mark_room_as_read(self, user, room):
        unread_messages_qs = user.unread_messages.filter(room=room)
        for message in unread_messages_qs:
            message.mark_as_read(user)
        return unread_messages_qs


class Message(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    room = models.ForeignKey(
        'Room',
        related_name='messages',
        on_delete=models.CASCADE)
    body = models.TextField(max_length=500, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    pending_reception = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='pending_messages')

    pending_read = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='unread_messages')

    front_key = models.UUIDField(
        verbose_name="frontend key",
        default=uuid.uuid4,
        unique=True)

    objects = MessageManager()

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return self.body

    def signal_to_room(self, message, data={}):
        for participant in self.room.participants.all():
            async_to_sync(channel_layer.group_send)(
                f"group_general_user_{participant.id}", {
                    "type": "chat_message",
                    "message": message,
                    'data': data
                })

    def remove_user_from_pending(self, user):
        if self.pending_reception.filter(id=user.id).exists():
            self.pending_reception.remove(user)
            # If there are no more pending then signal
            if not self.pending_reception.exists():
                self.signal_to_room('update_message', {
                    'message_id': self.id,
                    'kind': 'all_received'
                })

    def mark_as_read(self, user):
        if self.pending_read.filter(id=user.id).exists():
            self.pending_read.remove(user)
            # If there are no more pending then signal
            if not self.pending_read.exists():
                self.signal_to_room('update_message', {
                    'message_id': self.id,
                    'kind': 'all_read'
                })


class Room(models.Model):
    class RoomKind(models.IntegerChoices):
        PRIVATE = 1
        GROUP = 2

    group_name = models.CharField(max_length=255, blank=True, null=True)
    kind = models.IntegerField(choices=RoomKind.choices)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='rooms')

    created_at = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True)
    last_activity = models.DateTimeField(
        verbose_name='Last activity date',
        auto_now=True)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def signal_to_room(self, message, data={}):
        for participant in self.participants.all():
            async_to_sync(channel_layer.group_send)(
                f"group_general_user_{participant.id}", {
                    "type": "chat_message",
                    "message": message,
                    'data': data
                })
