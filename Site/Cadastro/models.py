from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Cliente(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length= 200)
    genero = (('M', 'Masculino'),
             ('F','Feminino'))
    sexo  = models.CharField(max_length=20,choices=genero)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse(f'{self.nome}')


class Produtos(models.Model):
     id = models.AutoField(primary_key=True)
     nome = models.CharField(max_length=20)
     decris = models.TextField(max_length=400)
     price = models.CharField(max_length=20)

     def __str__(self):
       return self.nome


     def get_absolute_url(self):

        return reverse(f'{self.nome}')