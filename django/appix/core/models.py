from django.db import models


class Vendedor(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=100, default="Sem detalhes", blank=False, null=False)
    delivery = models.BooleanField(default=False)
    retirada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
    
    def __str__(self):
        return f'{self.nome}'


    def quantidade_produtos(self):
        return self.produtos.count()


class Produto(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    observacao = models.CharField(max_length=100, default='Sem mais detalhes', blank=False, null=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='produtos')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'


class Comprador(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=134, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comprador'
        verbose_name_plural = 'Compradores'
    
    def __str__(self):
        return f'{self.nome} - {self.telefone}'


entrega_choices = [
    ('delivery', 'Delivery'),
    ('retirada', 'Retirada'),
]

class Venda(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='vendas')
    quantidade = models.IntegerField()
    entrega = models.CharField(max_length=100, choices=entrega_choices)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
    
    def __str__(self):
        return f'{self.id}'
    
    def vendedor(self):
        return self.produto.vendedor

    def valor_total(self):
        return f'R$ {self.produto.preco * self.quantidade}'