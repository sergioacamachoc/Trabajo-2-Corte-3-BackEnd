from django.db import models

# Create your models here.

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=120)
    salario = models.FloatField()

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return 
