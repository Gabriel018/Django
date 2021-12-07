from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente,Produtos

# Create your views here.

def init(request):


    return render(request,'init.html')

def cliente(request):
    clientview = Cliente.objects.all().count()

    context = {
        'clientview': clientview,

    }

    return  render(request,'clientes.html',context=context)


def produto(request):
    produtoview = Produtos.objects.all().count()

    context1 = {
        'produtoview': produtoview

    }

    return  render(request,'produtos.html',context=context1)