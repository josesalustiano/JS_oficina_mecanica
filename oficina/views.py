import base64
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from .models import Cliente, Veiculo
from .forms import ClienteForm, VeiculoForm
from .models import Cliente, Veiculo, Procedimento
from .forms import ClienteForm, VeiculoForm, ProcedimentoForm
from .models import Cliente, Veiculo, Procedimento, OrdemServico, Cobranca
from .forms import ClienteForm, VeiculoForm, ProcedimentoForm, OrdemServicoForm, CobrancaForm

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
        clientes_do_banco = Cliente.objects.filter(ativo=True)
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
        cliente.ativo = False
        cliente.save()

        Veiculo.objects.filter(cliente=cliente).update(ativo=False)
        
        return redirect('TelaClientes')

    return render(request, 'oficina/Cliente/ExcluirCliente.html', {'cliente': cliente})

# ==========================================
# MÓDULO DE VEÍCULOS
# ==========================================

def TelaVeiculos(request):
    veiculos_do_banco = Veiculo.objects.filter(ativo=True)
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

def DetalhesVeiculos(request, placa):
    veiculo = get_object_or_404(Veiculo, placa=placa)
    return render(request, 'oficina/Veiculo/DetalhesVeiculos.html', {'veiculo': veiculo})

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
    veiculo = get_object_or_404(Veiculo, placa=placa)
    
    if request.method == 'POST':
        veiculo.ativo = False
        veiculo.save()
        
        return redirect('TelaVeiculos')

    return render(request, 'oficina/Veiculo/ExcluirVeiculo.html', {'veiculo': veiculo})

def TelaProcedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'oficina/Procedimento/TelaProcedimentos.html', {'procedimentos': procedimentos})

def CadastrarProcedimento(request):
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TelaProcedimentos')
    else:
        form = ProcedimentoForm()
    return render(request, 'oficina/Procedimento/FormProcedimentos.html', {'form': form, 'titulo': 'Novo Procedimento'})

def EditarProcedimento(request, id):
    procedimento = get_object_or_404(Procedimento, id=id)
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST, instance=procedimento)
        if form.is_valid():
            form.save()
            return redirect('TelaProcedimentos')
    else:
        form = ProcedimentoForm(instance=procedimento)
    return render(request, 'oficina/Procedimento/FormProcedimentos.html', {'form': form, 'titulo': f'Editar Procedimento: {procedimento.nome}'})

def ExcluirProcedimento(request, id):
    procedimento = get_object_or_404(Procedimento, id=id)
    if request.method == 'POST':
        procedimento.delete()
        return redirect('TelaProcedimentos')
    return render(request, 'oficina/Procedimento/ExcluirProcedimento.html', {'procedimento': procedimento})

def TelaOS(request):
    # Trazemos todas as OS, ordenadas pelas mais recentes primeiro
    ordens = OrdemServico.objects.all().order_by('-data_criacao')
    return render(request, 'oficina/OS/TelaOS.html', {'ordens': ordens})

from .models import Cliente, Veiculo, Procedimento, OrdemServico, Cobranca # Garanta que Cobranca está aqui

def CadastrarOS(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            ordem = form.save(commit=False)
            if ordem.status == 'FINALIZADO':
                ordem.data_conclusao = timezone.now()
            ordem.save()
            
            # AUTOMAÇÃO: Se nasceu FINALIZADO, cria a cobrança automática
            if ordem.status == 'FINALIZADO':
                Cobranca.objects.get_or_create(
                    ordem_servico=ordem,
                    defaults={'valor_total': ordem.procedimento.valor}
                )
                
            return redirect('TelaOS')
    else:
        form = OrdemServicoForm()
    return render(request, 'oficina/OS/FormOS.html', {'form': form, 'titulo': 'Nova Ordem de Serviço'})

def EditarOS(request, id):
    ordem = get_object_or_404(OrdemServico, id=id)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)
        if form.is_valid():
            ordem_editada = form.save(commit=False)
            
            if ordem_editada.status == 'FINALIZADO':
                if not ordem_editada.data_conclusao:
                    ordem_editada.data_conclusao = timezone.now()
            else:
                ordem_editada.data_conclusao = None
                
            ordem_editada.save()
            
            # AUTOMAÇÃO: Se mudou o status para FINALIZADO na edição, cria a cobrança
            if ordem_editada.status == 'FINALIZADO':
                Cobranca.objects.get_or_create(
                    ordem_servico=ordem_editada,
                    defaults={'valor_total': ordem_editada.procedimento.valor}
                )
            else:
                # Opcional: Se reabrir a OS (mudar de Finalizado para Ativo), 
                # podemos deletar a cobrança se ela não estiver paga ainda
                if hasattr(ordem_editada, 'cobranca') and not ordem_editada.cobranca.paga:
                    ordem_editada.cobranca.delete()
                    
            return redirect('TelaOS')
    else:
        form = OrdemServicoForm(instance=ordem)
    return render(request, 'oficina/OS/FormOS.html', {'form': form, 'titulo': f'Editar OS #{ordem.id}'})
def DetalhesOS(request, id):
    ordem = get_object_or_404(OrdemServico, id=id)
    return render(request, 'oficina/OS/DetalhesOS.html', {'ordem': ordem})

def ExcluirOS(request, id):
    ordem = get_object_or_404(OrdemServico, id=id)
    if request.method == 'POST':
        ordem.delete()
        return redirect('TelaOS')
    return render(request, 'oficina/OS/ExcluirOS.html', {'ordem': ordem})

def TelaCobrancas(request):
    # Traz todas as cobranças geradas, mostrando as mais novas primeiro
    cobrancas = Cobranca.objects.all().order_by('-data_emissao', '-id')
    return render(request, 'oficina/Faturamento/TelaCobrancas.html', {'cobrancas': cobrancas})

def EditarCobranca(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca)
        if form.is_valid():
            form.save() # O save() customizado que fizemos no models vai atualizar o valor_total automaticamente!
            return redirect('TelaCobrancas')
    else:
        form = CobrancaForm(instance=cobranca)
    return render(request, 'oficina/Faturamento/FormCobranca.html', {'form': form, 'cobranca': cobranca})