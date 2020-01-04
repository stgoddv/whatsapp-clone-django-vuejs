from django.urls import path
from rest_framework import routers

from . import message, room

router = routers.SimpleRouter()
router.register(r'messages', message.MessageViewSet)
router.register(r'rooms', room.RoomViewSet)

urlpatterns = [
    path('messages/<int:room_id>', message.LastMessagesRoomAPIView.as_view()),
    path('rooms/recents', room.RecentRoomsAPIView.as_view()),
] + router.urls
