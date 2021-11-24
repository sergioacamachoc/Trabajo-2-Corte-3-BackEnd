from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Elaboracion
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class ElaboracionViewSet(viewsets.ModelViewSet):
    queryset = Elaboracion.objects.all()
    serializer_class = ElaboracionSerializer

    def list(self, request, *args, **kwargs):
        elaboraciones = Elaboracion.objects.all()
        serializer = ElaboracionMiniSerializer(elaboraciones, many=True)
        return Response(serializer.data)