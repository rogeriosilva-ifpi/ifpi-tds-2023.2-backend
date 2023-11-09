from django.http import HttpResponse, HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from devices.models import Ambiente
from devices.serializers import AmbienteSerializer

def hello(request: HttpRequest):
  return HttpResponse('OK, deu certo!')


class PingView(APIView):

  def get(self, request):
    return Response({'nome': 'Rogério'}, status=200)

  def post(self, request):
    # print('data', request.data)
    nome = request.data.get('nome') or 'Não Informada'
    return Response({'nome': nome}, status=201)


class AmbienteListCreateView(APIView):

  def get(self, request):
    ambientes = Ambiente.objects.all()
    serializer = AmbienteSerializer(ambientes, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = AmbienteSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AmbienteDetailUpdateView(APIView):

  def get(self, request, pk):
    try:
      ambiente = Ambiente.objects.get(pk=pk)
      serializer = AmbienteSerializer(ambiente)
      return Response(serializer.data)
    except:
      return Response(status=404)
  
  def put(self, request, pk):
    try:
      ambiente = Ambiente.objects.get(pk=pk)
      serializer = AmbienteSerializer(ambiente, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
      return Response(serializer.errors, status=400)
    except:
      return Response({'detail': 'Não localizado!'},status=404)
  

  def delete(self, request, pk):
    try:
      ambiente = Ambiente.objects.get(pk=pk)
      ambiente.delete()
      return Response(status=204)
    except:
      return Response({'detail': 'Não localizado!'},status=404)

