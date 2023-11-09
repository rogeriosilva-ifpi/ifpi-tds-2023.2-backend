
from django.contrib import admin
from django.urls import path, include
from devices.urls import urlpatterns as devices_urls

urlpatterns = [
    path('devices/', include(devices_urls)),
    path('admin/', admin.site.urls),
]
