from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import produto

# Create your views here.

def home(request):

    """template = loader.get_template('index.html')
    return HttpResponse(template.render())"""


    Protudos = produto.objects.all().values()

    return HttpResponse(Protudos)