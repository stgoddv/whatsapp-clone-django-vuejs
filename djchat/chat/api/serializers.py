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
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_last_message(self, obj):
        last_message = obj.messages.all().order_by('-timestamp').first()
        return MessageSerializer(last_message).data
