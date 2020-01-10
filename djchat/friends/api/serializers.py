from rest_framework import serializers

from django.contrib.auth import get_user_model

from friends.models import Friend, FriendshipRequest

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class FriendshipRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()

    class Meta:
        model = FriendshipRequest
        exclude = ('to_user', )


class FriendshipSentRequestSerializer(serializers.ModelSerializer):
    to_user = UserSerializer()

    class Meta:
        model = FriendshipRequest
        exclude = ('from_user', )
