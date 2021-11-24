"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from Empleado.views import *
from Empleado.views import *
from Pastelero.views import *
from Coccion.views import *
from Decorador.views import *
from Elaboracion.views import *
from Final.views import *
from Horno.views import *
from Ingredientes.views import *
from Solicitud.views import *

router = routers.DefaultRouter()
router.register(r'empleado', EmpleadoViewSet)
router.register(r'pastelero', PasteleroViewSet)
router.register(r'coccion', CoccionViewSet)
router.register(r'decorador', DecoradorViewSet)
router.register(r'elaboracion', ElaboracionViewSet)
router.register(r'final', FinalViewSet)
router.register(r'horno', HornoViewSet)
router.register(r'solicitud', SolicitudViewSet)
router.register(r'ingrediente', IngredienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
#EmpleadoViewSet.as_view({'get': 'list'})
