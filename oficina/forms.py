from django import forms
from .models import Cliente, Veiculo, Procedimento, OrdemServico, Cobranca

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # Listamos todos os campos que vão aparecer no seu FormClientes.html
        fields = ['nome', 'cpf', 'telefone', 'rua', 'numero', 'bairro']
        
        # Injetamos o estilo do Bootstrap direto nos inputs para ficarem bonitos
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(84) 99999-9999'}),
            'rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua ou Logradouro'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nº'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
        }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['cliente', 'placa', 'marca', 'modelo', 'ano', 'cor']
        
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select select2-search'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC-1234'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Fiat, VW...'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Uno, Gol...'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Preto, Vermelho...'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2020'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(ativo=True)    

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['nome', 'valor', 'tempo_estimado', 'descricao']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Troca de Óleo'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 150.00', 'step': '0.01'}),
            'tempo_estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 20 dias, 2 horas, 45 min'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalhes adicionais sobre o serviço...'}),
        }

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['veiculo', 'procedimento', 'status']
        
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'procedimento': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        # Permitimos editar apenas o valor adicional, as observações e o status de pagamento
        fields = ['valor_adicional', 'observacoes', 'paga']
        
        widgets = {
            'valor_adicional': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Ex: Adicionado R$ 50 referente ao óleo do motor e filtro.'}),
            'paga': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            'valor_adicional': 'Valor Adicional / Peças Extras (R$)',
            'observacoes': 'Justificativa do Valor Adicional',
            'paga': 'Marcar como CONFIRMADO / PAGO',
        }