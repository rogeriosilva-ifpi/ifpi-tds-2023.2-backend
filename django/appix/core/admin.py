from django.contrib import admin
from .models import Vendedor, Produto, Comprador, Venda


class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'quantidade_produtos', 'delivery', 'retirada']

    inlines = [ProdutoInline]
  

@admin.register(Comprador)
class CompradorAdmin(admin.ModelAdmin):
  pass


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = [ 'produto', 'quantidade', 'valor_total', 'vendedor', 'comprador']


# @admin.register(Produto)
# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = ['nome', 'observacao', 'preco']
