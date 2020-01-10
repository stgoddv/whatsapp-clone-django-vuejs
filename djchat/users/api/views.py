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
