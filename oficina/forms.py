from django import forms
from .models import Cliente, Veiculo, Procedimento

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
        fields = ['cliente', 'placa', 'marca', 'modelo', 'ano']
        
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC-1234'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Fiat, VW...'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Uno, Gol...'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2020'}),
        }

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['nome', 'valor', 'tempo_estimado_minutos', 'descricao']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Troca de Óleo'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 150.00', 'step': '0.01'}),
            'tempo_estimado_minutos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 60'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalhes adicionais sobre o serviço...'}),
        }