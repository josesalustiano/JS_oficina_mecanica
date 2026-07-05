from django.urls import path
from . import views

urlpatterns = [
    # Tela Inicial / Dashboard da Oficina (deixe a string vazia '' para ser a página principal)
    path('', views.dashboard, name='dashboard'),
    
    # Quando o utilizador aceder a /clientes/, chama a View lista_clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
]