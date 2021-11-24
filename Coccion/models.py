from django.db import models
from django.db.models.deletion import CASCADE
from Elaboracion.models import Elaboracion
from Horno.models import Horno
# Create your models here.

class Coccion(models.Model):
    elaboracion=models.OneToOneField(Elaboracion, on_delete=CASCADE)
    temperatura=models.FloatField()
    fechahora_inicio=models.DateTimeField()
    fechahora_final=models.DateTimeField()
    horno=models.OneToOneField(Horno, on_delete=CASCADE)
    
    def __str__(self):
        return self.elaboracion.__str__()