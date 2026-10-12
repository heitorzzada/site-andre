from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib import messages
from django.db.models import Q, Count, Sum
from braces.views import GroupRequiredMixin

from .models import PerfilUsuario, CategoriaServico, EstiloTatuagem, Servico, Tatuagem, Orcamento, Agendamento
from .forms import (
    UsuarioCadastroForm, PerfilUsuarioForm, CategoriaServicoForm,
    EstiloTatuagemForm, ServicoForm, TatuagemForm,
    OrcamentoForm, OrcamentoGestaoForm, AgendamentoForm, AgendamentoStatusForm
)


# ==============================================================================
# 1. PÁGINAS INSTITUCIONAIS & SOBRE (REQUISITO DO 1º TRIMESTRE)
# ==============================================================================

class HomeView(TemplateView):
    """
    Página inicial do Studio Oliveira.
    Utiliza QuerySets para trazer destaques, serviços otimizados e obras.
    """
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Otimização com select_related e filtros de destaque
        context['servicos_destaque'] = Servico.objects.filter(ativo=True, destaque=True).select_related('categoria')[:4]
        context['tatuagens_destaque'] = Tatuagem.objects.filter(destaque=True).select_related('estilo')[:8]
        context['estilos'] = EstiloTatuagem.objects.filter(ativo=True)
        context['total_obras'] = Tatuagem.objects.count()
        context['total_servicos'] = Servico.objects.filter(ativo=True).count()
        return context


class SobreView(TemplateView):
    """
    Página 'Sobre' exigida no 1º Trimestre do PDF:
    - Descrição do projeto em forma de texto
    - Diagrama de Casos de Uso (imagem)
    - Diagrama de Classes (imagem)
    """
    template_name = 'website/sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Sobre o Projeto — Studio Oliveira"
        context['disciplina'] = "Programação Web — 4º Ano"
        context['instituicao'] = "Instituto Federal do Paraná (IFPR)"
        context['professor'] = "Rafael Henrique Dalegrave Zottesso"
        return context


# ==============================================================================
# 2. AUTENTICAÇÃO E PERFIL (REQUISITO DO 2º TRIMESTRE)
# ==============================================================================

class UsuarioCadastroView(CreateView):
    """
    Cadastro de novos usuários/clientes no sistema.
    """
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Criar Conta no Studio Oliveira',
        'subtitulo': 'Cadastre-se para solicitar orçamentos e agendar suas sessões.',
        'botao': 'Cadastrar Minha Conta'
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adiciona o usuário ao grupo 'Cliente' automaticamente
        grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
        self.object.groups.add(grupo_cliente)
        messages.success(self.request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        return response


class LoginPersonalizadoView(LoginView):
    template_name = 'website/form.html'
    extra_context = {
        'titulo': 'Acessar Studio Oliveira',
        'subtitulo': 'Entre com seu usuário e senha.',
        'botao': 'Entrar no Sistema'
    }


class LogoutPersonalizadoView(LogoutView):
    next_page = reverse_lazy('home')


class AlterarSenhaPersonalizadaView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'website/form.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'titulo': 'Alterar Senha de Acesso',
        'subtitulo': 'Digite sua senha atual e escolha uma nova senha segura.',
        'botao': 'Atualizar Minha Senha'
    }

    def form_valid(self, form):
        messages.success(self.request, 'Sua senha foi alterada com sucesso!')
        return super().form_valid(form)


# ==============================================================================
# 3. CRUD CATEGORIA DE SERVIÇO
# ==============================================================================

class CategoriaList(ListView):
    model = CategoriaServico
    template_name = 'website/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self):
        qs = CategoriaServico.objects.all()
        busca = self.request.GET.get('busca')
        if busca:
            qs = qs.filter(Q(nome__icontains=busca) | Q(descricao__icontains=busca))
        return qs


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = ['Administrador', 'Gerente']
    model = CategoriaServico
    form_class = CategoriaServicoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('categoria-listar')
    extra_context = {'titulo': 'Cadastrar Categoria de Serviço', 'botao': 'Cadastrar Categoria'}


class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = ['Administrador', 'Gerente']
    model = CategoriaServico
    form_class = CategoriaServicoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('categoria-listar')
    extra_context = {'titulo': 'Editar Categoria de Serviço', 'botao': 'Atualizar Categoria'}


class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = ['Administrador', 'Gerente']
    model = CategoriaServico
    template_name = 'website/form-excluir.html'
    success_url = reverse_lazy('categoria-listar')
    extra_context = {'titulo': 'Excluir Categoria'}


# ==============================================================================
# 4. CRUD ESTILO DE TATUAGEM
# ==============================================================================

class EstiloList(ListView):
    model = EstiloTatuagem
    template_name = 'website/estilo_list.html'
    context_object_name = 'estilos'
    paginate_by = 10

    def get_queryset(self):
        qs = EstiloTatuagem.objects.all()
        busca = self.request.GET.get('busca')
        if busca:
            qs = qs.filter(Q(nome__icontains=busca) | Q(descricao__icontains=busca))
        return qs


class EstiloCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = ['Administrador', 'Gerente']
    model = EstiloTatuagem
    form_class = EstiloTatuagemForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('estilo-listar')
    extra_context = {'titulo': 'Cadastrar Estilo de Tatuagem', 'botao': 'Salvar Estilo'}


class EstiloUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = ['Administrador', 'Gerente']
    model = EstiloTatuagem
    form_class = EstiloTatuagemForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('estilo-listar')
    extra_context = {'titulo': 'Editar Estilo de Tatuagem', 'botao': 'Atualizar Estilo'}


class EstiloDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = ['Administrador', 'Gerente']
    model = EstiloTatuagem
    template_name = 'website/form-excluir.html'
    success_url = reverse_lazy('estilo-listar')
    extra_context = {'titulo': 'Excluir Estilo de Tatuagem'}


# ==============================================================================
# 5. CRUD SERVIÇO (OTIMIZADO COM SELECT_RELATED)
# ==============================================================================

class ServicoList(ListView):
    model = Servico
    template_name = 'website/servico_list.html'
    context_object_name = 'servicos'
    paginate_by = 6

    def get_queryset(self):
        # Otimização select_related
        qs = Servico.objects.select_related('categoria').all()
        busca = self.request.GET.get('busca')
        if busca:
            qs = qs.filter(Q(nome__icontains=busca) | Q(descricao__icontains=busca) | Q(categoria__nome__icontains=busca))
        return qs


class ServicoDetail(DetailView):
    model = Servico
    template_name = 'website/servico_detail.html'
    context_object_name = 'servico'


class ServicoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = ['Administrador', 'Gerente']
    model = Servico
    form_class = ServicoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('servico-listar')
    extra_context = {'titulo': 'Cadastrar Novo Serviço', 'botao': 'Cadastrar Serviço'}

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ServicoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = ['Administrador', 'Gerente']
    model = Servico
    form_class = ServicoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('servico-listar')
    extra_context = {'titulo': 'Editar Serviço', 'botao': 'Salvar Alterações'}


class ServicoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = ['Administrador', 'Gerente']
    model = Servico
    template_name = 'website/form-excluir.html'
    success_url = reverse_lazy('servico-listar')
    extra_context = {'titulo': 'Excluir Serviço'}


# ==============================================================================
# 6. CRUD TATUAGEM / GALERIA DE OBRAS
# ==============================================================================

class TatuagemList(ListView):
    model = Tatuagem
    template_name = 'website/tatuagem_list.html'
    context_object_name = 'tatuagens'
    paginate_by = 8

    def get_queryset(self):
        qs = Tatuagem.objects.select_related('estilo').all()
        estilo_slug = self.request.GET.get('estilo')
        busca = self.request.GET.get('busca')
        if estilo_slug:
            qs = qs.filter(estilo__slug=estilo_slug)
        if busca:
            qs = qs.filter(Q(titulo__icontains=busca) | Q(descricao__icontains=busca))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estilos'] = EstiloTatuagem.objects.filter(ativo=True)
        context['estilo_atual'] = self.request.GET.get('estilo', '')
        return context


class TatuagemDetail(DetailView):
    model = Tatuagem
    template_name = 'website/tatuagem_detail.html'
    context_object_name = 'tatuagem'


class TatuagemCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = ['Administrador', 'Gerente']
    model = Tatuagem
    form_class = TatuagemForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('tatuagem-listar')
    extra_context = {'titulo': 'Adicionar Nova Obra à Galeria', 'botao': 'Cadastrar Obra'}


class TatuagemUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = ['Administrador', 'Gerente']
    model = Tatuagem
    form_class = TatuagemForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('tatuagem-listar')
    extra_context = {'titulo': 'Editar Obra do Portfólio', 'botao': 'Salvar Alterações'}


class TatuagemDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = ['Administrador', 'Gerente']
    model = Tatuagem
    template_name = 'website/form-excluir.html'
    success_url = reverse_lazy('tatuagem-listar')
    extra_context = {'titulo': 'Excluir Obra da Galeria'}


# ==============================================================================
# 7. CRUD ORÇAMENTO (CLASSE 1 COM ISOLAMENTO RIGOROSO POR USUÁRIO)
# REQUISITO DO 2º E 3º TRIMESTRE
# ==============================================================================

class OrcamentoList(LoginRequiredMixin, ListView):
    """
    Listar: Lista apenas orçamentos do usuário logado (ou todos se for Administrador/Gerente).
    """
    model = Orcamento
    template_name = 'website/orcamento_list.html'
    context_object_name = 'orcamentos'
    paginate_by = 6

    def get_queryset(self):
        qs = Orcamento.objects.select_related('servico', 'estilo', 'usuario')
        # Regra de negócio: Administrador/Gerente vê tudo; Cliente só vê o seu próprio
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)

        busca = self.request.GET.get('busca')
        if busca:
            qs = qs.filter(Q(servico__nome__icontains=busca) | Q(descricao_ideia__icontains=busca) | Q(local_corpo__icontains=busca))
        return qs


class OrcamentoDetail(LoginRequiredMixin, DetailView):
    """
    Detalhar: Exibe apenas o orçamento do próprio usuário (ou qualquer um se for admin).
    """
    model = Orcamento
    template_name = 'website/orcamento_detail.html'
    context_object_name = 'orcamento'

    def get_queryset(self):
        qs = Orcamento.objects.select_related('servico', 'estilo', 'usuario')
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)
        return qs


class OrcamentoCreate(LoginRequiredMixin, CreateView):
    """
    Inserir: 'Guarda' o User autenticado no atributo usuario (form_valid).
    """
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('orcamento-listar')
    extra_context = {
        'titulo': 'Solicitar Novo Orçamento — Studio Oliveira',
        'subtitulo': 'Descreva sua ideia para receber a avaliação técnica de nossa equipe.',
        'botao': 'Enviar Solicitação de Orçamento'
    }

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Sua solicitação de orçamento foi enviada com sucesso!')
        return super().form_valid(form)


class OrcamentoUpdate(LoginRequiredMixin, UpdateView):
    """
    Editar: Permite que o User só edite seus próprios registros (get_queryset).
    """
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('orcamento-listar')
    extra_context = {'titulo': 'Editar Solicitação de Orçamento', 'botao': 'Atualizar Solicitação'}

    def get_queryset(self):
        qs = Orcamento.objects.all()
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)
        return qs


class OrcamentoDelete(LoginRequiredMixin, DeleteView):
    """
    Excluir: Permite que o User só exclua seus próprios registros (get_queryset).
    """
    model = Orcamento
    template_name = 'website/form-excluir.html'
    success_url = reverse_lazy('orcamento-listar')
    extra_context = {'titulo': 'Cancelar / Excluir Solicitação de Orçamento'}

    def get_queryset(self):
        qs = Orcamento.objects.all()
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)
        return qs


class OrcamentoGestaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    """
    View gerencial para Administrador/Gerente analisar, definir valor e parecer do estúdio.
    """
    group_required = ['Administrador', 'Gerente']
    model = Orcamento
    form_class = OrcamentoGestaoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('orcamento-listar')
    extra_context = {'titulo': 'Gestão & Análise de Orçamento', 'botao': 'Atualizar Parecer do Estúdio'}


# ==============================================================================
# 8. CRUD AGENDAMENTO (CLASSE 2 COM ISOLAMENTO POR USUÁRIO E O MOVIMENTO DO PROJETO)
# REQUISITO DO 1º, 2º E 3º TRIMESTRE
# ==============================================================================

class AgendamentoList(LoginRequiredMixin, ListView):
    """
    Listar o movimento (sessões agendadas):
    - Clientes só visualizam suas próprias sessões.
    - Gerentes e Administradores visualizam a agenda global do estúdio.
    """
    model = Agendamento
    template_name = 'website/agendamento_list.html'
    context_object_name = 'agendamentos'
    paginate_by = 6

    def get_queryset(self):
        qs = Agendamento.objects.select_related('servico', 'orcamento', 'usuario')
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)

        busca = self.request.GET.get('busca')
        if busca:
            qs = qs.filter(Q(servico__nome__icontains=busca) | Q(status__icontains=busca))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Relatório / Consulta agregada (Requisito da 2ª entrega do 2º Trimestre)
        user_agendamentos = self.get_queryset()
        context['total_agendamentos'] = user_agendamentos.count()
        context['concluidos'] = user_agendamentos.filter(status='concluido').count()
        context['valor_acumulado'] = user_agendamentos.filter(status='concluido').aggregate(Sum('valor_total'))['valor_total__sum'] or 0
        return context


class AgendamentoDetail(LoginRequiredMixin, DetailView):
    model = Agendamento
    template_name = 'website/agendamento_detail.html'
    context_object_name = 'agendamento'

    def get_queryset(self):
        qs = Agendamento.objects.select_related('servico', 'orcamento', 'usuario')
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)
        return qs


class AgendamentoCreate(LoginRequiredMixin, CreateView):
    """
    Criação do movimento de agendamento de sessão.
    Guarda o usuário autenticado em form_valid().
    """
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('agendamento-listar')
    extra_context = {
        'titulo': 'Agendar Sessão de Procedimento',
        'subtitulo': 'Escolha a data e o horário desejados para seu atendimento no Studio Oliveira.',
        'botao': 'Confirmar Agendamento'
    }

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Sessão agendada com sucesso! Aguarde a confirmação de nossa recepção.')
        return super().form_valid(form)


class AgendamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('agendamento-listar')
    extra_context = {'titulo': 'Editar Detalhes do Agendamento', 'botao': 'Salvar Alterações'}

    def get_queryset(self):
        qs = Agendamento.objects.all()
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)
        return qs


class AgendamentoDelete(LoginRequiredMixin, DeleteView):
    model = Agendamento
    template_name = 'website/form-excluir.html'
    success_url = reverse_lazy('agendamento-listar')
    extra_context = {'titulo': 'Cancelar Sessão Agendada'}

    def get_queryset(self):
        qs = Agendamento.objects.all()
        if not self.request.user.groups.filter(name__in=['Administrador', 'Gerente']).exists():
            qs = qs.filter(usuario=self.request.user)
        return qs


class AgendamentoConcluirView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    """
    Movimento Gerencial: Baixa e conclusão de atendimento com registro de cuidados pós-sessão.
    """
    group_required = ['Administrador', 'Gerente']
    model = Agendamento
    form_class = AgendamentoStatusForm
    template_name = 'website/form.html'
    success_url = reverse_lazy('agendamento-listar')
    extra_context = {
        'titulo': 'Concluir / Atualizar Status da Sessão',
        'subtitulo': 'Atualize o andamento do procedimento e registre as orientações de cicatrização.',
        'botao': 'Confirmar Conclusão da Sessão'
    }
