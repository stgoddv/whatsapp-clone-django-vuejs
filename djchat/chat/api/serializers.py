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
    group_name = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_last_message(self, obj):
        current_user = self.context['request'].user
        last_message = obj.messages.all().order_by('-timestamp').first()
        last_message.remove_user_from_pending(current_user)
        return last_message.id if last_message else None

    def get_group_name(self, obj):
        if obj.kind == 1:
            # If private then return name of the other participant
            current_user = self.context['request'].user
            participants = list(obj.participants.all())
            participants.remove(current_user)
            return participants[0].username
        return obj.group_name
