from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'bairro', 'cidade', 'telefone', 'usuario', 'criado_em')
    list_filter = ('categoria', 'porte', 'cidade', 'criado_em')
    search_fields = ('nome', 'raca', 'bairro', 'cidade', 'telefone', 'caracteristicas', 'descricao')
    readonly_fields = ('criado_em', 'atualizado_em')
