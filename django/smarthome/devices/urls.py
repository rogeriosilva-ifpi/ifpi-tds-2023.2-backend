from django.urls import path
from devices.views import hello, \
 PingView, AmbienteListCreateView, AmbienteDetailUpdateView

urlpatterns = [
  path('rogerio', hello),
  path('ping', PingView.as_view()),
  path('ambientes', AmbienteListCreateView.as_view()),
  path('ambientes/<int:pk>', AmbienteDetailUpdateView.as_view())
]