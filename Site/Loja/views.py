from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import produto

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def produtos(request):
    template = loader.get_template('produtos.html')
    Produtos = produto.objects.all().values()
    context = {
        'Produtos': Produtos,
    }
    return  HttpResponse(template.render(context,request))

def add(request):
    template  = loader.get_template('cad_prod.html')
    return HttpResponse(template.render({},request))

def add_record(request):
    x = request.POST['Desc']
    y = request.POST['Quant']

    prod = produto(Desc=x,Quant=y)
    prod.save()
    return HttpResponseRedirect('produtos')

def delete(request, id):
    Produtos  = produto.objects.get(id=id)
    Produtos.delete()
    return HttpResponse('Excluido com sucesso')

