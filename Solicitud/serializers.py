from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = (
            'nameSolicitud',
            'tipo', 
            'peso_minimo', 
            'fecha_solicitud',
            'fecha_entrega', 
            'descripcion', 
            'empleado', 
        ) 

class SolicitudMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id','nameSolicitud', 'tipo', 
            'peso_minimo', 
            'fecha_solicitud',
            'fecha_entrega', 
            'descripcion', 'empleado')