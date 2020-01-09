from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from django.contrib.auth import get_user_model

from users.api.serializers import UserSerializer

User = get_user_model()


class UsersAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)


class CurrentUserAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CreateInvitationAPIView(APIView):
    def post(self, request, format=None):
        # Validation by serialization
        # Two different existing users are required
        # Check if invitation already exists
        # Check if users have already a relationship
        # Create the invitation
        # Send invitation signal
        # Response OK
        pass


class InvitationViewSet(viewsets.ViewSet):
    pass
    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)


class AcceptInvitationAPIView(APIView):
    def post(self, request, format=None):
        pass


class DeclineInvitationAPIView(APIView):
    def post(self, request, format=None):
        pass


class FriendsViewSet(viewsets.ViewSet):
    pass


class DeleteFriendAPIView(APIView):
    def post(self, request, format=None):
        pass


class BlockFriendAPIView(APIView):
    def post(self, request, format=None):
        pass
