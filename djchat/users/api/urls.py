from django.urls import path
from users.api.views import CurrentUserAPIView, UsersAPIView

urlpatterns = [
    path('me', CurrentUserAPIView.as_view(), name='current-user'),
    path('users', UsersAPIView.as_view()),
]
