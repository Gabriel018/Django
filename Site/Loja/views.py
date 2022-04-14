from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import produto

# Create your views here.

def home(request):
    Produtos = produto.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'Produtos':Produtos,
    }
    return HttpResponse(template.render(context,request))


def produtos(request):
    template = loader.get_template('produtos.html')
    return  HttpResponse(template.render({},request))

def add(request):
    template  = loader.get_template('cad_prod.html')
    return HttpResponse(template.render({},request))
