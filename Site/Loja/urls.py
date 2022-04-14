from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='nome'),
    path('add',views.add, name='add'),
    path('produtos', views.produtos, name='produtos'),
]