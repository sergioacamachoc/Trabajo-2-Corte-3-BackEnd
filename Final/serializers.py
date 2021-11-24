from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Final

class FinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Final
        fields = (
            'coccion',
            'decorador', 
            'fechahora_inicio',
            'fechahora_final',
            'peso_final',
            'fecha_entrega',
        ) 

class FinalMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Final
        fields = ('id','coccion','decorador','fechahora_inicio',
            'fechahora_final', 'peso_final', 'fecha_entrega')