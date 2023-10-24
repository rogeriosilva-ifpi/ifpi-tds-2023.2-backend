from django.contrib import admin
from django.urls import include, path

from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include(core_urls))
]
