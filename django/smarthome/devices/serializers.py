from rest_framework.serializers import ModelSerializer, IntegerField
from devices.models import Ambiente, Dispositivo

class DispositivoSimplesSerializer(ModelSerializer):
  class Meta:
    model = Dispositivo
    fields = ['id', 'nome']


class AmbienteSerializer(ModelSerializer):

  dispositivos = DispositivoSimplesSerializer(many=True)
  contador_dispositivos = IntegerField(read_only=True, source='count_dispositivos')

  class Meta:
    model = Ambiente
    fields = '__all__'


class AmbienteSimplesSerializer(ModelSerializer):
  class Meta:
    model = Ambiente
    fields = ['nome']


class DispositivoSerializer(ModelSerializer):
  # ambiente = AmbienteSimplesSerializer()
  
  class Meta:
    model = Dispositivo
    fields = '__all__'