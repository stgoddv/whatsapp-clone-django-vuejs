from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from users.api.serializers import UserSerializer

User = get_user_model()


class UsersAPIView(APIView):
    def get(self, request):
        email = request.GET.get('email', '')
        user = get_object_or_404(User.objects.all(), email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CurrentUserAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
