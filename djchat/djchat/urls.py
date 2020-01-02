from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Chat API')

urlpatterns = [
    path('chat/', include('chat.urls')),

    path('api/v1/', include('chat.api.urls')),
    path('api/v1/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    path('', schema_view),
]
