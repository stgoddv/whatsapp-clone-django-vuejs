from django.urls import path
from rest_framework import routers

from . import messageViews, roomViews

router = routers.SimpleRouter()
router.register(r'messages', messageViews.MessageViewSet)
router.register(r'rooms', roomViews.RoomViewSet)

urlpatterns = [
    path('messages/<int:room_id>', messageViews.LastMessagesRoomAPIView.as_view()),
    path('messages/unread', messageViews.UnreadMessagesAPIView.as_view()),
    path('rooms/recents', roomViews.RecentRoomsAPIView.as_view()),
    path('rooms/<int:room_id>/writing', roomViews.RoomWritingAPIView.as_view()),
    path('rooms/<int:room_id>/read', roomViews.RoomMarkAsReadAPIView.as_view()),
] + router.urls
