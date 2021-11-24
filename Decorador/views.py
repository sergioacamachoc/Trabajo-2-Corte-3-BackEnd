from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Decorador
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class DecoradorViewSet(viewsets.ModelViewSet):
    queryset = Decorador.objects.all()
    serializer_class = DecoradorSerializer

    def list(self, request, *args, **kwargs):
        decoradores = Decorador.objects.all()
        serializer = DecoradorMiniSerializer(decoradores, many=True)
        return Response(serializer.data)