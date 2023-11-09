from rest_framework.serializers import ModelSerializer
from devices.models import Ambiente

class AmbienteSerializer(ModelSerializer):
  class Meta:
    model = Ambiente
    fields = '__all__'