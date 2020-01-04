from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import MessageSerializer, CreateMessageSerializer
from chat.models import Message, Room

channel_layer = get_channel_layer()


class MessageViewSet(viewsets.ViewSet):
    """
    Endpoints related to managing messages
    """
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer

    def list(self, request):
        """
        List user's pending to receive messages
        """
        pending_messages_qs = Message.objects\
            .get_pending_messages(request.user)
        serializer = MessageSerializer(pending_messages_qs, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create new message in backend and signal participants to receive it
        """
        user = request.user
        # Validation
        serializer = CreateMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = serializer.validated_data.get('room')
        if not user in room.participants.all():
            raise PermissionDenied(
                detail='Current user is not authorized to publish in the room')
        # Message creation
        message = serializer.save(
            author=user,
            pending_reception=room.participants.all())
        # Push to participants
        for participant in room.participants.all():
            async_to_sync(channel_layer.group_send)(
                f"group_general_user_{participant.id}", {
                    "type": "chat_message",
                    "message": "update"
                })
        return Response(serializer.data, status=status.HTTP_201_CREATED)
