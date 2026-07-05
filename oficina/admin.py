from django.contrib import admin
from .models import Cliente, Veiculo, Procedimento, OrdemServico, Cobranca, Pagamento

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Procedimento)
admin.site.register(OrdemServico)
admin.site.register(Cobranca)
admin.site.register(Pagamento)