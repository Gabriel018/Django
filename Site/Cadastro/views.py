from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from django.shortcuts import render
# Create your views here.

def init(request):
    clientview = Cliente.objects.all()

    return render(request,'init.html')