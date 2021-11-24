from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Decorador

class DecoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decorador
        fields = (
            'empleado',
            'n_pasaporteD', 
            'pais_origenD',
            'experienciaD',
        ) 

class DecoradorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decorador
        fields = ('id','empleado', 'n_pasaporteD' , 'pais_origenD',
            'experienciaD')