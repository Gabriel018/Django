from django.urls import path
from . import  views


urlpatterns = [
    path('', views.init,name='init'),
    path('clientes/',views.cliente, name='clientes')
]