from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from friends.exceptions import AlreadyExistsError, AlreadyFriendsError
from friends.models import Friend, Follow, FriendshipRequest, Block

from .serializers import (
    UserSerializer,
    FriendshipRequestSerializer,
    FriendshipSentRequestSerializer
)

user_model = get_user_model()


class MyFriendsAPIView(APIView):
    """ View my friends """

    def get(self, request, format=None):
        friends = Friend.objects.friends(request.user)
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)


class FriendsAPIView(APIView):
    """ View the friends of a user """

    def get(self, request, user_id, format=None):
        user = get_object_or_404(user_model, id=user_id)
        friends = Friend.objects.friends(user)
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)


class FriendshipAddAPIView(APIView):
    """ Create a FriendshipRequest """

    def post(self, request, user_id, format=None):
        to_user = user_model.objects.get(id=user_id)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            return Response({'detail': 'Friendship request already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except AlreadyFriendsError as e:
            return Response({'detail': 'The users are already friends.'}, status=status.HTTP_400_BAD_REQUEST)
        return FriendshipSentRequestListAPIView.get(self, request)


class FriendshipRemoveAPIView(APIView):
    """ Create a FriendshipRequest """

    def post(self, request, user_id, format=None):
        to_user = user_model.objects.get(id=user_id)
        from_user = request.user
        could_remove = Friend.objects.remove_friend(from_user, to_user)
        if could_remove:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Friendship not found.'}, status=status.HTTP_404_NOT_FOUND)


class FriendshipAcceptAPIView(APIView):
    """ Accept a friendship request """

    def get(self, request, friendship_request_id, format=None):
        return FriendshipRequestDetailAPIView.get(self, request, friendship_request_id=friendship_request_id)

    def post(self, request, friendship_request_id, format=None):
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id
        )
        f_request.accept()
        return FriendshipRequestListAPIView.get(self, request)


class FriendshipRejectAPIView(APIView):
    """ Reject a friendship request """

    def get(self, request, friendship_request_id, format=None):
        return FriendshipRequestDetailAPIView.get(self, request, friendship_request_id=friendship_request_id)

    def post(self, request, friendship_request_id, format=None):
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id
        )
        f_request.reject()
        return FriendshipRequestListAPIView.get(self, request)


class FriendshipCancelAPIView(APIView):
    """ Cancel a previously created friendship_request_id """

    def get(self, request, friendship_request_id, format=None):
        return FriendshipRequestDetailAPIView.get(self, request, friendship_request_id=friendship_request_id)

    def post(self, request, friendship_request_id, format=None):
        f_request = get_object_or_404(
            request.user.friendship_requests_sent, id=friendship_request_id
        )
        f_request.cancel()
        return FriendshipSentRequestListAPIView.get(self, request)


class FriendshipRequestListAPIView(APIView):
    """ View received friendship requests """

    def get(self, request, format=None):
        friendship_requests = Friend.objects.requests(request.user)
        serializer = FriendshipRequestSerializer(
            friendship_requests, many=True)
        return Response(serializer.data)


class FriendshipSentRequestListAPIView(APIView):
    """ View sent friendship requests """

    def get(self, request, format=None):
        friendship_requests = Friend.objects.sent_requests(request.user)
        serializer = FriendshipSentRequestSerializer(
            friendship_requests, many=True)
        return Response(serializer.data)


class FriendshipRequestListRejectedAPIView(APIView):
    """ View rejected friendship requests """

    def get(self, request, format=None):
        friendship_requests = Friend.objects.rejected_requests(request.user)
        serializer = FriendshipRequestSerializer(
            friendship_requests, many=True)
        return Response(serializer.data)


class FriendshipRequestDetailAPIView(APIView):
    """ View a particular friendship request """

    def get(self, request, friendship_request_id, format=None):
        f_request = get_object_or_404(
            FriendshipRequest, id=friendship_request_id)
        serializer = FriendshipRequestSerializer(
            f_request)
        return Response(serializer.data)
