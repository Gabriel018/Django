from django.urls import path
from . import  views


urlpatterns = [
    path('', views.cliente),
    path('cadastro/',views.cliente),
    path('cadastro/',views.produto)
]