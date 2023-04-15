from django.db import models
from alimentos.models import Food
# Create your models here.


TYPE_CYCLE = [
    ('DESAYUNO', 'desayuno'),
    ('MERIENDA', 'merienda'),
    ('ALMUERZO', 'almuerzo'),
    ('CENA', 'cena'),
]

class Reseta(models.Model):
    name = models.CharField(max_length=200)
    cycle = models.CharField(max_length=200, choices=TYPE_CYCLE)
    



class CantidadesReseta(models.Model):
    reseta = models.ForeignKey(Reseta, on_delete=models.CASCADE, )
    food = models.ForeignKey(Food, on_delete=models.CASCADE, )
    cantidad = models.IntegerField()
