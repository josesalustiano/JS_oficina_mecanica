from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    # Endereço simplificado diretamente no cadastro do cliente
    rua = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca.nome} {self.nome}"
    
class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50) # Ex: SUV, Hatch, Sedã
    cor = models.CharField(max_length=30)
    placa = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.modelo} - Placa: {self.placa}"