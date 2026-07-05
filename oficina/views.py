from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    # Vai ao banco de dados e pega todos os clientes
    clientes_do_banco = Cliente.objects.all() 
    
    # Manda esses clientes para um arquivo HTML
    return render(request, 'oficina/lista_clientes.html', {'clientes': clientes_do_banco})