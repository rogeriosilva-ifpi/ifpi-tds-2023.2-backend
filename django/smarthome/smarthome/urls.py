
from django.contrib import admin
from django.urls import path, include
from devices.urls import urlpatterns as devices_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('devices/', include(devices_urls)),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
