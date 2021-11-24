from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Empleado
from.serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def list(self, request, *args, **kwargs):
        empleados = Empleado.objects.all()
        serializer = EmpleadoMiniSerializer(empleados, many=True)
        return Response(serializer.data)

