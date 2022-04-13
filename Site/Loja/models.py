from django.db import models

# Create your models here.
class produto(models.Model):
    Desc = models.CharField(max_length=200)
    Quant = models.CharField(max_length=2)
