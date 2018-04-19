from django.db import models
from produto.models import produto, refeicao
from cliente.models import cliente
from django.utils import timezone

# Create your models here.
class refe_item(models.Model):
    id = models.AutoField(primary_key=True)
    refeicoes = models.ForeignKey(refeicao)
    quantidade = models.IntegerField(default='1')
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __int__(self):
        return self.id

class prod_item(models.Model):
    id = models.AutoField(primary_key=True)
    produtos = models.ForeignKey(produto)
    quantidade = models.IntegerField(default='1')
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __int__(self):
        return self.id

class pedido(models.Model):
    ESTADO = (
        ('1', 'Em Aberto'),
        ('2', 'Finalizada'),
    )
    METODO = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
    )
    id = models.AutoField(primary_key=True)
    cliente_pedido = models.ForeignKey(cliente)
    produto_item = models.ManyToManyField(prod_item)
    refeicao_item = models.ManyToManyField(refe_item)
    estado = models.CharField(max_length=1, choices=ESTADO)
    metodo = models.CharField(max_length=1, choices=METODO, null=True, blank=True)
    data_abertura = models.DateTimeField(default=timezone.now)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    desc = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)