from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Horno
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class HornoViewSet(viewsets.ModelViewSet):
    queryset = Horno.objects.all()
    serializer_class = HornoSerializer

    def list(self, request, *args, **kwargs):
        hornos = Horno.objects.all()
        serializer = HornoMiniSerializer(hornos, many=True)
        return Response(serializer.data)