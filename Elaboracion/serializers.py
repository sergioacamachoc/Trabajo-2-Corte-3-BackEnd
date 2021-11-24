from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Elaboracion

class ElaboracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elaboracion
        fields = (
            'solicitud',
            'pasteleros', 
            'ingredientes',
        ) 

class ElaboracionMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elaboracion
        fields = ('id','solicitud', 'pasteleros','ingredientes')