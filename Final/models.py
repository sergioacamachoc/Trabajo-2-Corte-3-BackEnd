from django.db import models
from django.db.models.deletion import CASCADE
from Coccion.models import Coccion
from Decorador.models import Decorador
# Create your models here.

class Final(models.Model):
    
    coccion=models.OneToOneField(Coccion, on_delete=CASCADE)
    decorador=models.OneToOneField(Decorador, on_delete=CASCADE)
    fechahora_inicio=models.DateTimeField()
    fechahora_final=models.DateTimeField()
    peso_final=models.FloatField()
    fecha_entrega=models.DateField()

    def __str__(self):
        return self.coccion.__str__()