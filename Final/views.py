from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Final
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class FinalViewSet(viewsets.ModelViewSet):
    queryset = Final.objects.all()
    serializer_class = FinalSerializer

    def list(self, request, *args, **kwargs):
        finales = Final.objects.all()
        serializer = FinalMiniSerializer(finales, many=True)
        return Response(serializer.data)