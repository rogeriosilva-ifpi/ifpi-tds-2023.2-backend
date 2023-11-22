from django.db import models

class Ambiente(models.Model):
  nome = models.CharField(max_length=100)
  atualizado_em = models.DateTimeField(auto_now=True)

  def count_dispositivos(self):
    return len(self.dispositivos.all())

  def __str__(self):
    return f'{self.nome}'


class Dispositivo(models.Model):
  nome = models.CharField(max_length=50)
  atualizado_em = models.DateTimeField(auto_now=True)

  ambiente = models.ForeignKey(Ambiente, 
    on_delete=models.CASCADE, related_name='dispositivos')
  
  def __str__(self):
    return f'{self.nome}'