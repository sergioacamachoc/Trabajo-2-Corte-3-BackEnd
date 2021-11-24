from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nameIngrediente=models.CharField(max_length=120)
    unidad_medida=models.CharField(max_length=120)
    cantidad=models.FloatField()

    def __str__(self):
        return self.name