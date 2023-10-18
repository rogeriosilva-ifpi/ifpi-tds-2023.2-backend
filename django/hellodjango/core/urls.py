from django.urls import path
from .views import hello, hello_rosa, milhao, index

urlpatterns = [
  path('', index),
  path('hello', hello),
  path('rosa', hello_rosa),
  path('milho', milhao)
]