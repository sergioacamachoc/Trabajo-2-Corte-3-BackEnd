from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pastelero

class PasteleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastelero
        fields = (
            'id',
            'empleado', 
            'n_pasaporteP',
            'pais_origenP',
            'experienciaP',
        )

class PasteleroMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastelero
        fields = ('id','empleado', 'n_pasaporteP', 'pais_origenP',
            'experienciaP',)