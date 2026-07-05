from django import forms
from .models import Cliente

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