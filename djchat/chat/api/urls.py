from rest_framework import routers

from . import message, room

router = routers.SimpleRouter()
router.register(r'messages', message.MessageViewSet)
router.register(r'rooms', room.RoomViewSet)

urlpatterns = router.urls
