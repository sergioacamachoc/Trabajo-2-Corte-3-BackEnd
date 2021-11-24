from django.db import models
from django.db.models.deletion import CASCADE
from Empleado.models import Empleado
# Create your models here.

class Decorador(models.Model):

    empleado=models.OneToOneField(Empleado, on_delete=CASCADE)
    n_pasaporteD=models.CharField(max_length=50, unique=1, blank=0)
    pais_origenD=models.CharField(max_length=50)
    experienciaD=models.FloatField(default=5)

    def __str__(self):
        return self.empleado.__str__()