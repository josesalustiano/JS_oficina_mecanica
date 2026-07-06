import base64
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from .models import Cliente, Veiculo
from .forms import ClienteForm, VeiculoForm

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

# ==========================================
# MÓDULO DE VEÍCULOS
# ==========================================

def TelaVeiculos(request):
    veiculos_do_banco = Veiculo.objects.all() 
    return render(request, 'oficina/Veiculo/TelaVeiculos.html', {'veiculos': veiculos_do_banco})

def CadastrarVeiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TelaVeiculos')
    else:
        form = VeiculoForm()
    return render(request, 'oficina/Veiculo/FormVeiculos.html', {'form': form, 'titulo': 'Novo Cadastro de Veículo'})

def EditarVeiculo(request, placa):
    # Agora procura pela placa em vez do id
    veiculo = get_object_or_404(Veiculo, placa=placa)
    
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('TelaVeiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    
    return render(request, 'oficina/Veiculo/FormVeiculos.html', {
        'form': form, 
        'veiculo': veiculo, 
        'titulo': f'Editar Veículo: {veiculo.placa}'
    })

def ExcluirVeiculo(request, placa):
    # Agora procura pela placa
    veiculo = get_object_or_404(Veiculo, placa=placa)
    
    if request.method == 'POST':
        veiculo.delete()
        return redirect('TelaVeiculos')
    return render(request, 'oficina/Veiculo/ExcluirVeiculo.html', {'veiculo': veiculo})