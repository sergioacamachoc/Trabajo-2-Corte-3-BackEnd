from django.db import models
from django.db.models.deletion import CASCADE
from Solicitud.models import Solicitud
from Pastelero.models import Pastelero
from Ingredientes.models import Ingrediente
# Create your models here.

class Elaboracion(models.Model):
    solicitud=models.OneToOneField(Solicitud, on_delete=CASCADE)
    pasteleros=models.ManyToManyField(Pastelero)
    ingredientes=models.ManyToManyField(Ingrediente)
    def __str__(self):
        return self.solicitud.__str__()