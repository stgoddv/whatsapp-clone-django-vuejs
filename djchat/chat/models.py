from django.db import models
from django.conf import settings


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

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"


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
