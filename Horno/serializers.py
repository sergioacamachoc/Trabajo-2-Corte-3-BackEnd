from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Horno

class HornoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horno
        fields = (
            'marca',
            'valor', 
        ) 

class HornoMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horno
        fields = ('id','marca', 'valor')