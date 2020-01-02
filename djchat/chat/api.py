from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MessageSerializer
from .models import Message

User = get_user_model()


class MessageViewSet(viewsets.ViewSet):
    """
    Endpoints related to managing messages
    """
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def list(self, request):
        """
        List user's pending to receive messages
        """
        pending_messages_qs = Message.objects\
            .get_pending_messages(request.user)
        serializer = MessageSerializer(pending_messages_qs, many=True)
        return Response(serializer.data)
