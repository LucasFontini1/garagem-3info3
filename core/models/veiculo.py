from django.db import models

from core.models import Acessorio, Cor, Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(s):
        return f'({s.id}), {s.modelo}, {s.cor}, {s.ano}'
