from rest_framework import serializers

from chat.models import Message, Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('pending_reception',)


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('room', 'body',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
