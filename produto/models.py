from django.db import models

# Create your models here.

class produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor_venda = models.DecimalField(max_digits=6, decimal_places=2)
    valor_compra = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    qnt_min = models.CharField(max_length=20, null=True, blank=True)
    quantidade = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class refeicao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.nome