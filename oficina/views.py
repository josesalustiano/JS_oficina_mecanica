from django.shortcuts import render, get_object_or_404
from .models import Cliente, Veiculo

def Dashboard(request):
    return render(request, 'oficina/Dashboard.html')

def TelaClientes(request):
    busca = request.GET.get('busca') 
    if busca:
        clientes_do_banco = Cliente.objects.filter(nome__icontains=busca) | Cliente.objects.filter(cpf__icontains=busca)
    else:
        clientes_do_banco = Cliente.objects.all() 
    
    return render(request, 'oficina/TelaClientes.html', {'clientes': clientes_do_banco})

def DetalhesClientes(request, cpf):
    cliente = get_object_or_404(Cliente, cpf=cpf)
    veiculos = cliente.veiculo_set.all()
    return render(request, 'oficina/DetalhesClientes.html', {'cliente': cliente, 'veiculos': veiculos})