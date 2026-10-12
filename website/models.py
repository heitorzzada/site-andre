from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class PerfilUsuario(models.Model):
    """
    Extensão do modelo User com informações complementares e grupo/perfil de acesso.
    """
    TIPO_CHOICES = [
        ('administrador', 'Administrador'),
        ('gerente', 'Gerente'),
        ('cliente', 'Cliente'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES, default='cliente', verbose_name='Tipo de Usuário')
    telefone = models.CharField(max_length=20, verbose_name='Telefone / WhatsApp')
    cpf = models.CharField(max_length=14, blank=True, null=True, verbose_name='CPF')
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True, verbose_name='Foto de Perfil')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Perfil de Usuário'
        verbose_name_plural = 'Perfis de Usuários'

    def __str__(self):
        return f"{self.usuario.get_full_name() or self.usuario.username} ({self.get_tipo_usuario_display()})"


class CategoriaServico(models.Model):
    """
    Classe 1: Categorias dos serviços oferecidos pelo Studio Oliveira.
    """
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')
    descricao = models.TextField(verbose_name='Descrição')
    icone = models.CharField(max_length=50, default='fa-palette', help_text='Classe FontAwesome ou identificador de ícone', verbose_name='Ícone')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria de Serviço'
        verbose_name_plural = 'Categorias de Serviços'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('categoria-listar')


class EstiloTatuagem(models.Model):
    """
    Classe 2: Estilos artísticos da galeria do Studio Oliveira.
    """
    nome = models.CharField(max_length=80, unique=True, verbose_name='Nome do Estilo')
    slug = models.SlugField(max_length=80, unique=True, verbose_name='Identificador (Slug)')
    descricao = models.TextField(verbose_name='Descrição do Estilo')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Estilo de Tatuagem'
        verbose_name_plural = 'Estilos de Tatuagens'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('estilo-listar')


class Servico(models.Model):
    """
    Classe 3: Procedimentos e serviços especializados do estúdio.
    """
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.PROTECT, related_name='servicos', verbose_name='Categoria')
    nome = models.CharField(max_length=120, verbose_name='Nome do Procedimento')
    descricao = models.TextField(verbose_name='Descrição Detalhada')
    preco_base = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço Base Estimado (R$)')
    duracao_minutos = models.PositiveIntegerField(default=60, verbose_name='Duração Estimada (Minutos)')
    ativo = models.BooleanField(default=True, verbose_name='Disponível para Atendimento')
    destaque = models.BooleanField(default=False, verbose_name='Exibir em Destaque na Home')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cadastrado por')
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['categoria', 'nome']

    def __str__(self):
        return f"{self.nome} - R$ {self.preco_base}"

    def get_absolute_url(self):
        return reverse('servico-listar')


class Tatuagem(models.Model):
    """
    Classe 4: Acervo de obras e portfólio artístico do Studio Oliveira.
    """
    titulo = models.CharField(max_length=120, verbose_name='Título da Obra')
    estilo = models.ForeignKey(EstiloTatuagem, on_delete=models.PROTECT, related_name='obras', verbose_name='Estilo Artístico')
    descricao = models.TextField(verbose_name='Descrição Técnica da Tatuagem')
    imagem_url = models.CharField(max_length=255, verbose_name='Caminho da Imagem', help_text='Caminho estático ou URL da imagem')
    destaque = models.BooleanField(default=False, verbose_name='Destaque na Página Inicial')
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Obra de Tatuagem'
        verbose_name_plural = 'Obras de Tatuagens'
        ordering = ['-cadastrado_em']

    def __str__(self):
        return f"{self.titulo} ({self.estilo.nome})"

    def get_absolute_url(self):
        return reverse('tatuagem-listar')


class Orcamento(models.Model):
    """
    Classe 5: Solicitação de orçamento enviada pelo cliente.
    REQUISITO DO PDF: Classe que separa objetos por usuário (somente quem cadastrou edita/exclui/lista).
    """
    STATUS_CHOICES = [
        ('pendente', 'Pendente de Análise'),
        ('em_analise', 'Em Análise pelo Estúdio'),
        ('aprovado', 'Aprovado / Pronto para Agendar'),
        ('recusado', 'Recusado / Ajustes Necessários'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orcamentos', verbose_name='Cliente Solicitante')
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, related_name='orcamentos', verbose_name='Serviço Pretendido')
    estilo = models.ForeignKey(EstiloTatuagem, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Estilo de Preferência')
    local_corpo = models.CharField(max_length=80, verbose_name='Local do Corpo (Ex: Antebraço, Costas...)')
    tamanho_estimado = models.CharField(max_length=80, verbose_name='Tamanho Estimado (Ex: 10 a 15 cm)')
    descricao_ideia = models.TextField(verbose_name='Descrição da Ideia e Significado')
    foto_referencia = models.ImageField(upload_to='referencias/', blank=True, null=True, verbose_name='Imagem de Referência (Opcional)')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', verbose_name='Status do Orçamento')
    valor_estimado = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Valor Estimado pelo Estúdio (R$)')
    resposta_estudio = models.TextField(blank=True, null=True, verbose_name='Parecer da Direção Técnica')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Data de Solicitação')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        verbose_name = 'Solicitação de Orçamento'
        verbose_name_plural = 'Solicitações de Orçamentos'
        ordering = ['-criado_em']

    def __str__(self):
        return f"Orçamento #{self.id} - {self.servico.nome} ({self.usuario.username}) - {self.get_status_display()}"

    def get_absolute_url(self):
        return reverse('orcamento-listar')


class Agendamento(models.Model):
    """
    Classe 6: O MOVIMENTO DO SISTEMA.
    Agendamento e sessão com fluxo completo de estados, cálculo financeiro e regras de negócio.
    REQUISITO DO PDF: Segunda classe que separa objetos por usuário.
    """
    STATUS_CHOICES = [
        ('solicitado', 'Sessão Solicitada'),
        ('confirmado', 'Confirmado pelo Estúdio'),
        ('em_andamento', 'Procedimento em Execução'),
        ('concluido', 'Sessão Concluída com Sucesso'),
        ('cancelado', 'Sessão Cancelada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos', verbose_name='Cliente')
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, related_name='agendamentos', verbose_name='Procedimento')
    orcamento = models.ForeignKey(Orcamento, on_delete=models.SET_NULL, null=True, blank=True, related_name='agendamentos', verbose_name='Orçamento Vinculado (Opcional)')
    data_agendada = models.DateField(verbose_name='Data Agendada')
    horario = models.TimeField(verbose_name='Horário da Sessão')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='solicitado', verbose_name='Status do Atendimento')
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor Total da Sessão (R$)')
    observacoes_sessao = models.TextField(blank=True, null=True, verbose_name='Observações Técnicas da Sessão')
    cuidados_pos_procedimento = models.TextField(blank=True, null=True, verbose_name='Instruções de Pós-Atendimento e Cicatrização')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Agendamento de Sessão (Movimento)'
        verbose_name_plural = 'Agendamentos de Sessões (Movimento)'
        ordering = ['-data_agendada', '-horario']

    def __str__(self):
        return f"Sessão #{self.id}: {self.servico.nome} - {self.data_agendada} às {self.horario} [{self.get_status_display()}]"

    def get_absolute_url(self):
        return reverse('agendamento-listar')
