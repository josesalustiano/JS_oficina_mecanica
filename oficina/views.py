import base64
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def decodificar_id(hash_id):
    try:
        return base64.urlsafe_b64decode(hash_id.encode('utf-8')).decode('utf-8')
    except:
        return None

def Dashboard(request):
    return render(request, 'oficina/Dashboard.html')

def TelaClientes(request):
    busca = request.GET.get('busca') 
    if busca:
        clientes_do_banco = Cliente.objects.filter(nome__icontains=busca) | Cliente.objects.filter(cpf__icontains=busca)
    else:
        clientes_do_banco = Cliente.objects.all() 
    # Apontando para a nova subpasta Cliente
    return render(request, 'oficina/Cliente/TelaClientes.html', {'clientes': clientes_do_banco})

def DetalhesClientes(request, hash_id):
    cpf_real = decodificar_id(hash_id)
    cliente = get_object_or_404(Cliente, cpf=cpf_real)
    veiculos = cliente.veiculo_set.all()
    # Apontando para a nova subpasta Cliente
    return render(request, 'oficina/Cliente/DetalhesClientes.html', {'cliente': cliente, 'veiculos': veiculos})

def CadastrarCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TelaClientes')
    else:
        form = ClienteForm()
    # Usando o novo FormClientes unificado
    return render(request, 'oficina/Cliente/FormClientes.html', {'form': form, 'titulo': 'Novo Cadastro de Cliente'})

def EditarCliente(request, hash_id):
    cpf_real = decodificar_id(hash_id)
    cliente = get_object_or_404(Cliente, cpf=cpf_real)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('TelaClientes')
    else:
        form = ClienteForm(instance=cliente)
    # Usando o mesmo FormClientes, mas passando um título diferente e o objeto cliente
    return render(request, 'oficina/Cliente/FormClientes.html', {'form': form, 'cliente': cliente, 'titulo': f'Editar Dados: {cliente.nome}'})

def ExcluirCliente(request, hash_id):
    cpf_real = decodificar_id(hash_id)
    cliente = get_object_or_404(Cliente, cpf=cpf_real)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('TelaClientes')
    # Apontando para a nova subpasta Cliente
    return render(request, 'oficina/Cliente/ExcluirCliente.html', {'cliente': cliente})