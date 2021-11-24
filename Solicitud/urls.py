from django.urls import path
from .views import *

app_name='Solicitud'
urlpatterns=[
    path('', inicio, name='inicio'),
]