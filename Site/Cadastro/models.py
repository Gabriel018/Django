from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True,blank=True)
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length= 200)
    email = models.CharField(max_length=200)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
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