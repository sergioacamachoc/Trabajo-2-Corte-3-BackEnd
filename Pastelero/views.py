from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Pastelero
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class PasteleroViewSet(viewsets.ModelViewSet):
    queryset = Pastelero.objects.all()
    serializer_class = PasteleroSerializer

    def list(self, request, *args, **kwargs):
        pasteleros = Pastelero.objects.all()
        serializer = PasteleroMiniSerializer(pasteleros, many=True)
        return Response(serializer.data)