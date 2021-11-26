from django.db import models
import uuid

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length= 200)
    genero = (('M', 'Masculino'),
             ('F','Feminino'))
    sexo  = models.CharField(max_length=20,choices=genero)

    def __str__(self):
        return self.nome



