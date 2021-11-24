from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Coccion

class CoccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coccion
        fields = (
            'elaboracion',
            'temperatura', 
            'fechahora_inicio',
            'fechahora_final',
            'horno',
        )

class CoccionMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coccion
        fields = ('id','elaboracion', 'temperatura','fechahora_inicio',
            'fechahora_final',
            'horno')