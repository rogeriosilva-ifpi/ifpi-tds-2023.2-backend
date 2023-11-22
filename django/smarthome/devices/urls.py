from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbienteViewSet, DispositivoViewSet

router = DefaultRouter()
router.register(r'ambientes', AmbienteViewSet)
router.register(r'dispositivos', DispositivoViewSet)

urlpatterns = [path('', include(router.urls))]



# urlpatterns = [
#   # path('ambientes', AmbienteListCreateView.as_view()),
#   # path('ambientes/<int:pk>', AmbienteDetailUpdateView.as_view()),
#   path('', include(router.urls)),
#   # path('dispositivos/', DispositivoListCreateView.as_view()),
#   # path('dispositivos/<int:pk>', DispositivoDetailUpdateDeleteView.as_view())
# ]