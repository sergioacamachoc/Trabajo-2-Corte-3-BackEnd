from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Coccion
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class CoccionViewSet(viewsets.ModelViewSet):
    queryset = Coccion.objects.all()
    serializer_class = CoccionSerializer

    def list(self, request, *args, **kwargs):
        cocciones = Coccion.objects.all()
        serializer = CoccionMiniSerializer(cocciones, many=True)
        return Response(serializer.data)