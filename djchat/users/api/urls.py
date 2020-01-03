from django.urls import path
from users.api.views import CurrentUserAPIView

urlpatterns = [
    path('me/', CurrentUserAPIView.as_view(), name='current-user')
]
