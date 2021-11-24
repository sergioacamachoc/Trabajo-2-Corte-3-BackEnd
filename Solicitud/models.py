from django.db import models
from django.db.models.deletion import CASCADE
from Empleado.models import Empleado
# Create your models here.

class Solicitud(models.Model):
    nameSolicitud=models.CharField(max_length=120)
    tipo=models.CharField(max_length=100)
    peso_minimo=models.CharField(max_length=50)
    fecha_solicitud=models.DateField()
    fecha_entrega=models.DateField()
    descripcion=models.TextField()
    empleado=models.OneToOneField(Empleado, on_delete=CASCADE)
    
    def __str__(self):
        return self.name