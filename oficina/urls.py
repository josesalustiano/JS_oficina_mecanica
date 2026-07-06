from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('clientes/', views.TelaClientes, name='TelaClientes'),
    path('clientes/cadastrar/', views.CadastrarCliente, name='CadastrarCliente'),
    # Note que agora usamos <str:hash_id> para receber o código seguro
    path('clientes/<str:hash_id>/', views.DetalhesClientes, name='DetalhesClientes'),
    path('clientes/<str:hash_id>/editar/', views.EditarCliente, name='EditarCliente'),
    path('clientes/<str:hash_id>/excluir/', views.ExcluirCliente, name='ExcluirCliente'),
    path('veiculos/', views.TelaVeiculos, name='TelaVeiculos'),
    path('veiculos/cadastrar/', views.CadastrarVeiculo, name='CadastrarVeiculo'),
    path('veiculos/<str:placa>/detalhes/', views.DetalhesVeiculos, name='DetalhesVeiculos'),
    path('veiculos/<str:placa>/editar/', views.EditarVeiculo, name='EditarVeiculo'),
    path('veiculos/<str:placa>/excluir/', views.ExcluirVeiculo, name='ExcluirVeiculo'),

    path('procedimentos/', views.TelaProcedimentos, name='TelaProcedimentos'),
    path('procedimentos/cadastrar/', views.CadastrarProcedimento, name='CadastrarProcedimento'),
    path('procedimentos/<int:id>/editar/', views.EditarProcedimento, name='EditarProcedimento'),
    path('procedimentos/<int:id>/excluir/', views.ExcluirProcedimento, name='ExcluirProcedimento'),
]