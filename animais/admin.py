from django.contrib import admin
from .models import PublicacaoPet

@admin.register(PublicacaoPet)
class PublicacaoPetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'status', 'bairro', 'usuario', 'criado_em')
    list_filter = ('categoria', 'status', 'bairro', 'criado_em')
    search_fields = ('nome', 'tipo_animal', 'bairro', 'contato', 'caracteristicas')
