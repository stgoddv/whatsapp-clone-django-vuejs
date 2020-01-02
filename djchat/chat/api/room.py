from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError

from chat.serializers import RoomSerializer
from chat.models import Room


class RoomViewSet(viewsets.ViewSet):
    """
    Endpoints related to managing rooms
    """
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        """
        List rooms in which the current user is a participant
        """
        serializer = RoomSerializer(request.user.rooms.all(), many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        get (private kind) or create a new room with participants
        """
        user = request.user
        # Validation of fields
        serializer = RoomSerializer(data=request.data)
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
                return Response(RoomSerializer(room_qs).data, status=status.HTTP_200_OK)
        # Create room
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
