from django.db import models
from django.conf import settings


class MessageManager(models.Manager):
    def get_pending_messages(self, user):
        pending_messages_qs = user.pending_messages.all()
        for message in pending_messages_qs:
            message.remove_user_from_pending(user)
        return pending_messages_qs


class Message(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE)
    body = models.TextField(max_length=500, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    pending_reception = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='pending_messages')

    objects = MessageManager()

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return self.body

    def remove_user_from_pending(self, user):
        self.pending_reception.remove(user)


class Room(models.Model):
    class RoomKind(models.IntegerChoices):
        PRIVATE = 1
        GROUP = 2

    kind = models.IntegerField(choices=RoomKind.choices)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='rooms')

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
