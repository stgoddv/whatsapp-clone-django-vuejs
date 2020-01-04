from rest_framework import serializers
from django.contrib.auth import get_user_model

from chat.models import Message, Room

User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    imOwner = serializers.SerializerMethodField()

    class Meta:
        model = Message
        exclude = ('pending_reception',)

    def get_imOwner(self, obj):
        user = self.context['request'].user
        return True if obj.author.id == user.id else False


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('room', 'body',)


class RoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_last_message(self, obj):
        last_message = obj.messages.all().order_by('-timestamp').first()
        return MessageSerializer(last_message, context=self.context).data
