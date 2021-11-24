from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id','nombre', 'salario')

class EmpleadoMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id','nombre', 'salario')