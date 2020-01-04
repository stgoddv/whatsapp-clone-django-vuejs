from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UsersAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
