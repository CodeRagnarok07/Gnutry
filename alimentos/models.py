from django.db import models
from .models import Food , Presentacion 

# Create your models here.
TYPE_FOOD = [
    ('CARBOHIDRATO', 'carbohidratos'),
    ('GRASA', 'grasas'),
    ('PROTEINA', 'proteina'),
]

class Food(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE_FOOD)
    calorias = models.IntegerField(help_text="por cada 100g")
    proteina = models.IntegerField(help_text="por cada 100g")

class Presentacion(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, )
    precio = models.IntegerField()
    cantidad = models.IntegerField()
