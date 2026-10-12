from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario, CategoriaServico, EstiloTatuagem, Servico, Tatuagem, Orcamento, Agendamento


class UsuarioCadastroForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, label="Nome")
    last_name = forms.CharField(max_length=50, required=True, label="Sobrenome")
    email = forms.EmailField(required=True, label="E-mail")
    telefone = forms.CharField(max_length=20, required=True, label="WhatsApp / Telefone")
    cpf = forms.CharField(max_length=14, required=False, label="CPF (Opcional)")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirmação de Senha")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password_confirm')
        if p1 and p2 and p1 != p2:
            self.add_error('password_confirm', 'As senhas digitadas não conferem.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            PerfilUsuario.objects.create(
                usuario=user,
                telefone=self.cleaned_data['telefone'],
                cpf=self.cleaned_data.get('cpf', ''),
                tipo_usuario='cliente'
            )
        return user


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['telefone', 'cpf', 'foto']


class CategoriaServicoForm(forms.ModelForm):
    class Meta:
        model = CategoriaServico
        fields = ['nome', 'descricao', 'icone', 'ativo']


class EstiloTatuagemForm(forms.ModelForm):
    class Meta:
        model = EstiloTatuagem
        fields = ['nome', 'slug', 'descricao', 'ativo']


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['categoria', 'nome', 'descricao', 'preco_base', 'duracao_minutos', 'ativo', 'destaque']


class TatuagemForm(forms.ModelForm):
    class Meta:
        model = Tatuagem
        fields = ['titulo', 'estilo', 'descricao', 'imagem_url', 'destaque']


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['servico', 'estilo', 'local_corpo', 'tamanho_estimado', 'descricao_ideia', 'foto_referencia']


class OrcamentoGestaoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['status', 'valor_estimado', 'resposta_estudio']


class AgendamentoForm(forms.ModelForm):
    data_agendada = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data Agendada")
    horario = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Horário")

    class Meta:
        model = Agendamento
        fields = ['servico', 'orcamento', 'data_agendada', 'horario', 'valor_total', 'observacoes_sessao', 'cuidados_pos_procedimento']


class AgendamentoStatusForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['status', 'observacoes_sessao', 'cuidados_pos_procedimento']
