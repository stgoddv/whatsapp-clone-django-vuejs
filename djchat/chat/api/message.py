from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from chat.serializers import MessageSerializer, CreateMessageSerializer
from chat.models import Message, Room

User = get_user_model()


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
        user = request.user
        content = request.data
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
        # Return OK
        return Response(serializer.data, status=status.HTTP_201_CREATED)