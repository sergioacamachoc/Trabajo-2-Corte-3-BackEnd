from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = (
            'nameIngrediente',
            'unidad_medida', 
            'cantidad', 
        ) 

class IngredienteMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id','nameIngrediente', 'unidad_medida', 'cantidad')