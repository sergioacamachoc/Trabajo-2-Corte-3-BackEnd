from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Solicitud
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    def list(self, request, *args, **kwargs):
        soliciudes = Solicitud.objects.all()
        serializer = SolicitudMiniSerializer(soliciudes, many=True)
        return Response(serializer.data)