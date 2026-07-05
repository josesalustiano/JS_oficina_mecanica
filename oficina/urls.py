from django.urls import path
from . import views

urlpatterns = [
    # Quando o utilizador aceder a /clientes/, chama a View lista_clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
]