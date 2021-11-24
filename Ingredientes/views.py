from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Ingrediente
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def list(self, request, *args, **kwargs):
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteMiniSerializer(ingredientes, many=True)
        return Response(serializer.data)