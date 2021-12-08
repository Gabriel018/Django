from django.urls import path
from . import  views


urlpatterns = [
    path('', views.cliente),
    path('cadastro/',views.cliente),
    path('client_cad/',views.client_cad),
    path('client_cad/submit', views.form_client),
    path('client_cad/delete/<int:id>', views.delet_client)
]