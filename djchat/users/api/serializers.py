from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'tagline',)
        read_only_fields = ['username', 'email']
