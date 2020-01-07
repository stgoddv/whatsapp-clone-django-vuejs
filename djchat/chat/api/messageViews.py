from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import MessageSerializer, CreateMessageSerializer, \
    RoomSerializer, UnreadMessageSerializer

from users.api.serializers import UserSerializer
from chat.models import Message, Room

channel_layer = get_channel_layer()
User = get_user_model()


class UnreadMessagesAPIView(APIView):
    """
    Endpoints related unread messages
    """
    queryset = Message.objects.all()

    def get(self, request, format=None):
        """
        List unread messages for a specific user
        """
        unread_messages_serializer = UnreadMessageSerializer(
            request.user.unread_messages.all(),
            context={'request': request},
            many=True)
        return Response({
            'messages': unread_messages_serializer.data
        })

    def post(self, request, format=None):
        """
        Mark an specific message as read
        """
        try:
            message_id = request.query_params.get('message_id')
            message_obj = request.user.unread_messages.get(id=message_id)
            message_obj.mark_as_read(request.user)
        except:
            # Simply avoid error msgs in this endpoint
            pass
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LastMessagesRoomAPIView(APIView):
    """
    Endpoints related to managing rooms with recent activity
    """
    queryset = Message.objects.all()

    def get(self, request, room_id, format=None):
        """
        List rooms with recent conversations
        """
        # get room
        room = get_object_or_404(request.user.rooms.all(), id=room_id)
        room_serializer = RoomSerializer(
            room,
            context={'request': request})
        # get messages
        offset = self.request.query_params.get('offset')
        offset = int(offset) if offset else None
        if offset:
            messages = room.messages    \
                .filter(id__lt=offset)  \
                .order_by('-id')[:10][::-1]
        else:
            messages = room.messages.order_by(
                '-timestamp')[:10][::-1]
        messages_serializer = MessageSerializer(
            messages,
            context={'request': request},
            many=True)
        # get participants
        participants = set()
        for message in messages_serializer.data:
            participants.add(message['author'])
        participants_obj = User.objects.filter(id__in=participants)
        users_serializer = UserSerializer(participants_obj, many=True)
        # combine response
        return Response({
            'messages': messages_serializer.data,
            'room': room_serializer.data,
            'users': users_serializer.data,
        })


class MessageViewSet(viewsets.ViewSet):
    """
    Endpoints related to managing messages
    """
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer

    def list(self, request):
        """
        List user's pending to receive messages
        """
        pending_messages_qs = Message.objects\
            .get_pending_messages(request.user)
        messages_serializer = MessageSerializer(pending_messages_qs,
                                                context={'request': request},
                                                many=True)
        # get relations of the rooms
        rooms = set()
        for message_data in messages_serializer.data:
            rooms.add(message_data['room'])
        rooms_obj = Room.objects.filter(id__in=rooms)
        rooms_serializer = RoomSerializer(rooms_obj,
                                          context={'request': request},
                                          many=True)
        # get relations of the users
        users = set()
        for room_data in rooms_serializer.data:
            users = users.union(set(room_data['participants']))
        users_obj = User.objects.filter(id__in=users)
        users_serializer = UserSerializer(users_obj, many=True)
        # combine response
        return Response({
            'messages': messages_serializer.data,
            'rooms': rooms_serializer.data,
            'users': users_serializer.data,
        })

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
            pending_reception=room.participants.all(),
            pending_read=room.participants.exclude(id=request.user.id))
        # Update activity timestamp of rooms
        room.save()
        # Push to participants
        for participant in room.participants.all():
            async_to_sync(channel_layer.group_send)(
                f"group_general_user_{participant.id}", {
                    "type": "chat_message",
                    "message": "update"
                })
        return Response(serializer.data, status=status.HTTP_201_CREATED)
