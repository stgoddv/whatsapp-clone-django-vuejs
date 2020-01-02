from django.urls import path
from rest_framework import routers

from . import views
from . import api

router = routers.SimpleRouter()
router.register(r'messages/pending', api.MessageViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
] + router.urls
