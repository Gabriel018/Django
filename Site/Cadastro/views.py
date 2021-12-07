from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente,Produtos

# Create your views here.

def init(request):


    return render(request,'init.html')

def cliente(request):
    cliente = Cliente.objects.all()

    dados = {'clientes': cliente, }

    return  render(request,'init.html',dados)


def produto(request):
    produtoview = Produtos.objects.all().count()

    context = {
        'produtoview': produtoview

    }

    return  render(request,'model-header.html',context=context)