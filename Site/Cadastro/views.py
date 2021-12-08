from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cliente,Produtos

# Create your views here.

def init(request):

    return render(request,'init.html')

def cliente(request):
    cliente = Cliente.objects.all()
    dados = {'clientes': cliente, }
    return  render(request,'init.html',dados)


def client_cad(request):
    id = request.GET.get('id')
    dados = {}
    if  id :
        dados['cliente'] = Cliente.objects.get(id=id)

    return  render(request,'cliente_cadastro.html',dados)

def form_client(request):
    if request.POST:
        id_cliente = request.POST.get('id')
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        if id_cliente:
           Cliente.objects.filter(id=id_cliente).update(nome=nome,idade=idade,email=email)

        else:
            Cliente.objects.create(nome=nome, idade=idade, email=email)

    return redirect('/')


def delet_client(request,id):

    Cliente.objects.filter(id=id).delete()
    return redirect('/')
