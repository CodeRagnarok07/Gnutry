from django.db import models

# Create your models here.
TYPE_FOOD = [
    ('CARBOHIDRATO', 'carbohidrato'),
    ('GRASA', 'grasa'),
    ('PROTEINA', 'proteina'),
]

class Origen(models.Model):
    name = models.CharField(max_length=200)


class Food(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE_FOOD)
    calorias = models.IntegerField(help_text="por cada 100g")
    proteina = models.IntegerField(help_text="por cada 100g")

class Presentacion(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, )
    origen = models.ForeignKey(Origen, on_delete=models.CASCADE, )
    precio = models.IntegerField()
    cantidad = models.IntegerField()
