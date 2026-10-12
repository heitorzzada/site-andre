from django.contrib import admin
from .models import PerfilUsuario, CategoriaServico, EstiloTatuagem, Servico, Tatuagem, Orcamento, Agendamento


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_usuario', 'telefone', 'cpf', 'criado_em')
    list_filter = ('tipo_usuario',)
    search_fields = ('usuario__username', 'usuario__email', 'telefone', 'cpf')


@admin.register(CategoriaServico)
class CategoriaServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'ativo', 'cadastrado_em')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')


@admin.register(EstiloTatuagem)
class EstiloTatuagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'ativo')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ('nome', 'descricao')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco_base', 'duracao_minutos', 'ativo', 'destaque')
    list_filter = ('categoria', 'ativo', 'destaque')
    search_fields = ('nome', 'descricao')


@admin.register(Tatuagem)
class TatuagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estilo', 'destaque', 'cadastrado_em')
    list_filter = ('estilo', 'destaque')
    search_fields = ('titulo', 'descricao')


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'servico', 'estilo', 'local_corpo', 'status', 'valor_estimado', 'criado_em')
    list_filter = ('status', 'servico', 'estilo')
    search_fields = ('usuario__username', 'local_corpo', 'descricao_ideia')


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'servico', 'data_agendada', 'horario', 'status', 'valor_total')
    list_filter = ('status', 'data_agendada')
    search_fields = ('usuario__username', 'servico__nome')
