from django.urls import path

from .views import (
    MyFriendsAPIView,
    FriendsAPIView,
    FriendshipAddAPIView,
    FriendshipRemoveAPIView,
    FriendshipAcceptAPIView,
    FriendshipRejectAPIView,
    FriendshipCancelAPIView,
    FriendshipRequestListAPIView,
    FriendshipSentRequestListAPIView,
    FriendshipRequestListRejectedAPIView,
    FriendshipRequestDetailAPIView
)

urlpatterns = [
    path('friends', MyFriendsAPIView.as_view(),
         name="friendship_view_my_friends"),

    path('friends/<int:user_id>', FriendsAPIView.as_view(),
         name="friendship_view_friends"),

    path('friends/add/<int:user_id>', FriendshipAddAPIView.as_view(),
         name="friendship_add_friend"),

    path('friends/remove/<int:user_id>', FriendshipRemoveAPIView.as_view(),
         name="friendship_remove_friends"),

    path('friends/requests/accept/<int:friendship_request_id>',
         FriendshipAcceptAPIView.as_view(), name="friendship_accept"),

    path('friends/requests/reject/<int:friendship_request_id>',
         FriendshipRejectAPIView.as_view(), name="friendship_reject"),

    path('friends/requests/cancel/<int:friendship_request_id>',
         FriendshipCancelAPIView.as_view(), name="friendship_cancel"),

    path('friends/requests/received',
         FriendshipRequestListAPIView.as_view(), name="friendship_request_list"),

    path('friends/requests/sent',
         FriendshipSentRequestListAPIView.as_view(), name="friendship_sent_request_list"),

    path('friends/requests/rejected',
         FriendshipRequestListRejectedAPIView.as_view(), name="friendship_requests_rejected"),

    path('friends/requests/<int:friendship_request_id>',
         FriendshipRequestDetailAPIView.as_view(), name="friendship_requests_detail"),

]
