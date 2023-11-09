from django.contrib import admin
from devices.models import Ambiente, Dispositivo

class DispositivoAdminInline(admin.TabularInline):
  model = Dispositivo
  extra = 1

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
  list_display = ['id', 'nome', 'atualizado_em']

  inlines = [DispositivoAdminInline]
