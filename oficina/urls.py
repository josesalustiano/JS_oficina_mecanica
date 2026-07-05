from django.urls import path
from . import views

urlpatterns = [
    # Tela Inicial / Dashboard da Oficina (deixe a string vazia '' para ser a página principal)
    path('', views.Dashboard, name='Dashboard'),
    
    # Quando o utilizador aceder a /clientes/, chama a View lista_clientes
    path('clientes/', views.TelaClientes, name='TelaClientes'),
    path('clientes/<str:cpf>/', views.DetalhesClientes, name='DetalhesClientes'),
]