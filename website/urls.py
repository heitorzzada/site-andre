from django.urls import path
from . import views

urlpatterns = [
    # Institucional e Página "Sobre" (1º Trimestre)
    path('', views.HomeView.as_view(), name='home'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),

    # Autenticação e Usuários (2º Trimestre)
    path('entrar/', views.LoginPersonalizadoView.as_view(), name='login'),
    path('sair/', views.LogoutPersonalizadoView.as_view(), name='logout'),
    path('cadastrar/', views.UsuarioCadastroView.as_view(), name='cadastrar'),
    path('alterar-senha/', views.AlterarSenhaPersonalizadaView.as_view(), name='alterar-senha'),

    # 1. Categoria de Serviço (CRUD)
    path('categoria/cadastrar/', views.CategoriaCreate.as_view(), name='categoria-cadastrar'),
    path('categoria/editar/<int:pk>/', views.CategoriaUpdate.as_view(), name='categoria-editar'),
    path('categoria/excluir/<int:pk>/', views.CategoriaDelete.as_view(), name='categoria-excluir'),
    path('categoria/listar/', views.CategoriaList.as_view(), name='categoria-listar'),

    # 2. Estilo de Tatuagem (CRUD)
    path('estilo/cadastrar/', views.EstiloCreate.as_view(), name='estilo-cadastrar'),
    path('estilo/editar/<int:pk>/', views.EstiloUpdate.as_view(), name='estilo-editar'),
    path('estilo/excluir/<int:pk>/', views.EstiloDelete.as_view(), name='estilo-excluir'),
    path('estilo/listar/', views.EstiloList.as_view(), name='estilo-listar'),

    # 3. Serviço (CRUD + Detail)
    path('servico/cadastrar/', views.ServicoCreate.as_view(), name='servico-cadastrar'),
    path('servico/editar/<int:pk>/', views.ServicoUpdate.as_view(), name='servico-editar'),
    path('servico/excluir/<int:pk>/', views.ServicoDelete.as_view(), name='servico-excluir'),
    path('servico/detalhar/<int:pk>/', views.ServicoDetail.as_view(), name='servico-detalhar'),
    path('servico/listar/', views.ServicoList.as_view(), name='servico-listar'),

    # 4. Tatuagem / Galeria (CRUD + Detail)
    path('tatuagem/cadastrar/', views.TatuagemCreate.as_view(), name='tatuagem-cadastrar'),
    path('tatuagem/editar/<int:pk>/', views.TatuagemUpdate.as_view(), name='tatuagem-editar'),
    path('tatuagem/excluir/<int:pk>/', views.TatuagemDelete.as_view(), name='tatuagem-excluir'),
    path('tatuagem/detalhar/<int:pk>/', views.TatuagemDetail.as_view(), name='tatuagem-detalhar'),
    path('tatuagem/listar/', views.TatuagemList.as_view(), name='tatuagem-listar'),

    # 5. Orçamento (CRUD + Detail + Isolamento por Usuário)
    path('orcamento/solicitar/', views.OrcamentoCreate.as_view(), name='orcamento-cadastrar'),
    path('orcamento/editar/<int:pk>/', views.OrcamentoUpdate.as_view(), name='orcamento-editar'),
    path('orcamento/excluir/<int:pk>/', views.OrcamentoDelete.as_view(), name='orcamento-excluir'),
    path('orcamento/detalhar/<int:pk>/', views.OrcamentoDetail.as_view(), name='orcamento-detalhar'),
    path('orcamento/listar/', views.OrcamentoList.as_view(), name='orcamento-listar'),
    path('orcamento/gestao/<int:pk>/', views.OrcamentoGestaoUpdate.as_view(), name='orcamento-gestao'),

    # 6. Agendamento - O MOVIMENTO (CRUD + Detail + Isolamento por Usuário)
    path('agendamento/novo/', views.AgendamentoCreate.as_view(), name='agendamento-cadastrar'),
    path('agendamento/editar/<int:pk>/', views.AgendamentoUpdate.as_view(), name='agendamento-editar'),
    path('agendamento/cancelar/<int:pk>/', views.AgendamentoDelete.as_view(), name='agendamento-excluir'),
    path('agendamento/detalhar/<int:pk>/', views.AgendamentoDetail.as_view(), name='agendamento-detalhar'),
    path('agendamento/listar/', views.AgendamentoList.as_view(), name='agendamento-listar'),
    path('agendamento/concluir/<int:pk>/', views.AgendamentoConcluirView.as_view(), name='agendamento-concluir'),
]
