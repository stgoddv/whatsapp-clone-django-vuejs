from django.core.management.base import BaseCommand, CommandError
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


class Command(BaseCommand):
    help = 'Send push notifications to clients'

    def handle(self, *args, **options):
        async_to_sync(channel_layer.group_send)(
            "chat_general", {
                "type": "chat_message",
                "message": "testeando esto"
            })
        self.stdout.write(self.style.SUCCESS('hola'))
