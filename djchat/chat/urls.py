from django.urls import path
from rest_framework import routers

from . import views
from .api import message, room

router = routers.SimpleRouter()
router.register(r'api/messages', message.MessageViewSet)
router.register(r'api/rooms', room.RoomViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
] + router.urls
