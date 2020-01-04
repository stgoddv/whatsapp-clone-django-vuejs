from django.urls import path
from rest_framework import routers

from . import message, room

router = routers.SimpleRouter()
router.register(r'messages', message.MessageViewSet)
router.register(r'rooms', room.RoomViewSet)

urlpatterns = [
    path('rooms/recents', room.RecentRoomsViewSet.as_view()),
] + router.urls
