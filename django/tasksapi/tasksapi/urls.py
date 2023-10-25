from django.contrib import admin
from django.urls import path, include
from tasks.urls import urlpatterns as tasks_urls

urlpatterns = [
    path('tasks/', include(tasks_urls)),
    path('admin/', admin.site.urls),
]
