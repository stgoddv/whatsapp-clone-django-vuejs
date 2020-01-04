from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from users.api.serializers import UserSerializer
from .serializers import RoomSerializer
from chat.models import Room

User = get_user_model()


class RecentRoomsAPIView(APIView):
    """
    Endpoints related to managing rooms with recent activity
    """
    queryset = Room.objects.all()

    def get(self, request, format=None):
        """
        List rooms with recent conversations
        """
        # get recent rooms
        qs_rooms = request.user.rooms.all().order_by('-last_activity')[:10]
        room_serializer = RoomSerializer(
            data=qs_rooms,
            context={'request': request},
            many=True)
        # get participants of the rooms
        participants = set()
        for room_data in room_serializer.data:
            participants = participants.union(set(room_data['participants']))
        participants_obj = User.objects.filter(id__in=participants)
        users_serializer = UserSerializer(participants_obj, many=True)
        # combine response
        return Response({
            'rooms': room_serializer.data,
            'users': users_serializer.data
        })


class RoomViewSet(viewsets.ViewSet):
    """
    Endpoints related to managing rooms
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        """
        List rooms in which the current user is a participant
        """
        # get all rooms
        qs_rooms = request.user.rooms.all()
        room_serializer = RoomSerializer(
            data=qs_rooms,
            context={'request': request},
            many=True)
        # get participants of the rooms
        participants = set()
        for room_data in room_serializer.data:
            participants = participants.union(set(room_data['participants']))
        participants_obj = User.objects.filter(id__in=participants)
        users_serializer = UserSerializer(participants_obj, many=True)
        # combine response
        return Response({
            'rooms': room_serializer.data,
            'users': users_serializer.data
        })

    def create(self, request):
        """
        get (private kind) or create a new room with participants
        """
        user = request.user
        # Validation of fields
        serializer = RoomSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        participants = serializer.validated_data.get('participants')
        if not user in participants:
            participants.append(user)
        if len(participants) == 1:
            raise ParseError(
                detail='There must be at least one another participant.')
        # Validate by kind
        kind = serializer.validated_data.get('kind')
        if (kind == 1):
            # Private chats must have 2 participants
            if len(participants) != 2:
                raise ParseError(
                    detail='Private chats must have exactly 2 participants.')
            # There cant be two private chats with same participants
            room_qs = Room.objects\
                .filter(kind=kind, participants__in=[participants[0]])\
                .filter(kind=kind, participants__in=[participants[1]])\
                .first()
            # If there exists private room return it
            if room_qs:
                return Response(RoomSerializer(data=room_qs, context={'request': request}).data, status=status.HTTP_200_OK)
        # Create room
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
