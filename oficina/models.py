from django.db import models
import base64

class Cliente(models.Model):
    # Mudança: CPF agora é a chave primária (ID) do Cliente
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    rua = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    @property
    def id_seguro(self):
        # Transforma o CPF num código Base64 seguro para URL
        return base64.urlsafe_b64encode(self.cpf.encode('utf-8')).decode('utf-8')

class Veiculo(models.Model):
    # Mudança: Placa agora é a chave primária (ID) do Veículo
    placa = models.CharField(max_length=10, primary_key=True)
    # Relação com o Cliente usa o CPF dele por baixo dos panos automaticamente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50, default="")
    modelo = models.CharField(max_length=50, default="")
    ano = models.IntegerField()
    categoria = models.CharField(max_length=50, blank=True, null=True) 
    cor = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}"

class Procedimento(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tempo_estimado_minutos = models.IntegerField(help_text="Tempo estimado em minutos")
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('SUSPENSO', 'Suspenso/Desativado'),
        ('FINALIZADO', 'Finalizado'),
    ]
    # A OS agora aponta diretamente para a Placa do Veículo
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ATIVO')

    def __str__(self):
        return f"OS #{self.id} - Placa: {self.veiculo.placa} ({self.status})"

class Cobranca(models.Model):
    ordem_servico = models.OneToOneField(OrdemServico, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_emissao = models.DateField(auto_now_add=True)
    # Campo auxiliar para os relatórios que você pediu de "Pagamentos em Aberto"
    paga = models.BooleanField(default=False) 

    def __str__(self):
        return f"Cobrança da OS #{self.ordem_servico.id} - Paga: {self.paga}"

class Pagamento(models.Model):
    cobranca = models.ForeignKey(Cobranca, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    metodo_pagamento = models.CharField(max_length=50)

    def __str__(self):
        return f"Pagamento de R$ {self.valor_pago} para OS #{self.cobranca.ordem_servico.id}"