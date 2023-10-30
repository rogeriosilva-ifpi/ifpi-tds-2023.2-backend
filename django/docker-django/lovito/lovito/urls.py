from django.contrib import admin
from django.urls import include, path

from core.urls import urlspatterns as core_urls

urlpatterns = [
	path('', include(core_urls)),
	path('admin/', admin.site.urls),
]
