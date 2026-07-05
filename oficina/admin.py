from django.contrib import admin
from .models import Cliente, Marca, Modelo, Veiculo, Procedimento, OrdemServico, Cobranca, Pagamento

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Veiculo)
admin.site.register(Procedimento)
admin.site.register(OrdemServico)
admin.site.register(Cobranca)
admin.site.register(Pagamento)