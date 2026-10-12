import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studio_oliveira_project.settings')
django.setup()

from django.contrib.auth.models import User, Group
from website.models import (
    PerfilUsuario, CategoriaServico, EstiloTatuagem, Servico,
    Tatuagem, Orcamento, Agendamento
)
from datetime import date, time

print("--- INICIANDO SEEDING DE DADOS DO STUDIO OLIVEIRA ---")

# 1. Grupos de Usuários
grp_admin, _ = Group.objects.get_or_create(name='Administrador')
grp_gerente, _ = Group.objects.get_or_create(name='Gerente')
grp_cliente, _ = Group.objects.get_or_create(name='Cliente')
print("[OK] Grupos criados: Administrador, Gerente, Cliente")

# 2. Usuários
# Admin
if not User.objects.filter(username='admin').exists():
    user_admin = User.objects.create_superuser('admin', 'admin@studiooliveira.com.br', 'admin123')
    user_admin.first_name = 'André'
    user_admin.last_name = 'de Oliveira'
    user_admin.save()
    user_admin.groups.add(grp_admin)
    PerfilUsuario.objects.create(
        usuario=user_admin,
        tipo_usuario='administrador',
        telefone='(11) 94486-3323',
        cpf='111.222.333-44'
    )
    print("[OK] Superusuário 'admin' criado (senha: admin123)")

# Gerente
if not User.objects.filter(username='gerente').exists():
    user_gerente = User.objects.create_user('gerente', 'joao@studiooliveira.com.br', 'gerente123')
    user_gerente.first_name = 'João Pedro'
    user_gerente.last_name = 'Santos Barbosa'
    user_gerente.save()
    user_gerente.groups.add(grp_gerente)
    PerfilUsuario.objects.create(
        usuario=user_gerente,
        tipo_usuario='gerente',
        telefone='(11) 94486-3323',
        cpf='222.333.444-55'
    )
    print("[OK] Usuário 'gerente' criado (senha: gerente123)")

# Cliente Teste
if not User.objects.filter(username='cliente').exists():
    user_cliente = User.objects.create_user('cliente', 'cliente@exemplo.com', 'cliente123')
    user_cliente.first_name = 'Lucas'
    user_cliente.last_name = 'Menezes'
    user_cliente.save()
    user_cliente.groups.add(grp_cliente)
    PerfilUsuario.objects.create(
        usuario=user_cliente,
        tipo_usuario='cliente',
        telefone='(11) 98765-4321',
        cpf='333.444.555-66'
    )
    print("[OK] Usuário 'cliente' criado (senha: cliente123)")

admin_user = User.objects.get(username='admin')
cliente_user = User.objects.get(username='cliente')

# 3. Categorias de Serviços
cat_tattoo, _ = CategoriaServico.objects.get_or_create(
    nome="Tatuagem Artística",
    defaults={
        "descricao": "Projetos autorais e exclusivos executados com agulhas descartáveis de precisão cirúrgica.",
        "icone": "fa-pen-nib",
        "ativo": True
    }
)

cat_piercing, _ = CategoriaServico.objects.get_or_create(
    nome="Body Piercing Profissional",
    defaults={
        "descricao": "Perfurações corporais estéreis com joalheria em Titânio ASTM F-136 e Ouro 18k biocompatíveis.",
        "icone": "fa-ring",
        "ativo": True
    }
)

cat_laser, _ = CategoriaServico.objects.get_or_create(
    nome="Remoção a Laser",
    defaults={
        "descricao": "Remoção total e clareamento de pigmentos com tecnologia Q-Switched e Nd:YAG preservando a pele.",
        "icone": "fa-bolt",
        "ativo": True
    }
)

cat_estetica, _ = CategoriaServico.objects.get_or_create(
    nome="Estética Reparadora",
    defaults={
        "descricao": "Reconstrução 3D de aréolas pós-mastectomia, camuflagem paramédica e Laser CO₂ Fracionado.",
        "icone": "fa-heart",
        "ativo": True
    }
)
print("[OK] Categorias de serviços registradas.")

# 4. Estilos de Tatuagem
est_realismo, _ = EstiloTatuagem.objects.get_or_create(
    slug="realismo",
    defaults={"nome": "Realismo & Colorido", "descricao": "Profundidade fotográfica, luz volumétrica e texturas hiper-realistas.", "ativo": True}
)
est_fineline, _ = EstiloTatuagem.objects.get_or_create(
    slug="fineline",
    defaults={"nome": "Fineline & Delicada", "descricao": "Traços milimétricos 1RL com precisão botânica e elegância atemporal.", "ativo": True}
)
est_blackwork, _ = EstiloTatuagem.objects.get_or_create(
    slug="blackwork",
    defaults={"nome": "Blackwork & Geométrico", "descricao": "Preto puro, mandalas, pontilhismo sagrado e contraste de alto impacto.", "ativo": True}
)
est_oriental, _ = EstiloTatuagem.objects.get_or_create(
    slug="oriental",
    defaults={"nome": "Oriental Clássico", "descricao": "Tradição milenar ukiyo-e com dragões, carpas, samurais e peônias.", "ativo": True}
)
est_geek, _ = EstiloTatuagem.objects.get_or_create(
    slug="geek",
    defaults={"nome": "Geek & Anime", "descricao": "Cenas épicas de mangás, animes e games com fidelidade estética absoluta.", "ativo": True}
)
print("[OK] Estilos artísticos registrados.")

# 5. Serviços do Estúdio
s1, _ = Servico.objects.get_or_create(
    nome="Tatuagem Autoral Exclusiva",
    defaults={
        "categoria": cat_tattoo,
        "descricao": "Desenvolvimento e tatuagem de projeto autoral sob medida com estudo anatômico.",
        "preco_base": 650.00,
        "duracao_minutos": 180,
        "ativo": True,
        "destaque": True,
        "usuario": admin_user
    }
)
s2, _ = Servico.objects.get_or_create(
    nome="Body Piercing em Titânio Grau Implante",
    defaults={
        "categoria": cat_piercing,
        "descricao": "Perfuração com assepsia estéril e aplicação de joia em titânio polido espelhado.",
        "preco_base": 180.00,
        "duracao_minutos": 45,
        "ativo": True,
        "destaque": True,
        "usuario": admin_user
    }
)
s3, _ = Servico.objects.get_or_create(
    nome="Sessão de Remoção de Tatuagem a Laser",
    defaults={
        "categoria": cat_laser,
        "descricao": "Disparo de pulso ultracurto Nd:YAG Q-Switched para fragmentação dérmica de tinta.",
        "preco_base": 350.00,
        "duracao_minutos": 40,
        "ativo": True,
        "destaque": True,
        "usuario": admin_user
    }
)
s4, _ = Servico.objects.get_or_create(
    nome="Reconstrução Areolar 3D & Camuflagem",
    defaults={
        "categoria": cat_estetica,
        "descricao": "Pigmentação paramédica de alta complexidade para restauração visual de aréolas e cicatrizes.",
        "preco_base": 800.00,
        "duracao_minutos": 120,
        "ativo": True,
        "destaque": True,
        "usuario": admin_user
    }
)
print("[OK] Serviços especializados registrados.")

# 6. Obras da Galeria (Portfólio Studio Oliveira)
obras_data = [
    ("Venom Hiper-Realista", est_realismo, "Trabalho hiper-realista com profundidade e contraste cinematográfico.", "images/paulo-tattoo-1.jpeg", True),
    ("Águia Realista em Sombras", est_realismo, "Sombreamento preto e cinza com riqueza anatômica e luz volumétrica.", "images/paulo-tattoo-2.jpeg", True),
    ("Rã Tropical Viva", est_realismo, "Realismo colorido vibrante com pigmentação de saturação pura.", "images/paulo-tattoo-3.jpeg", False),
    ("Goku Black Rosé", est_geek, "Linhas fiéis ao estilo de animação com degradê magenta brilhante.", "images/raffa-tattoo-1.jpeg", True),
    ("Golden Frieza Cósmico", est_geek, "Cores metálicas douradas e roxas com iluminação de energia.", "images/raffa-tattoo-2.jpeg", False),
    ("Dragão Oriental Tradicional", est_oriental, "Composição clássica japonesa com escamas precisas e movimento fluido.", "images/attila-tattoo-1.png", True),
    ("Carpa Koi & Flor de Lótus", est_oriental, "Símbolo de perseverança com movimento de água e equilíbrio de sombras.", "images/attila-tattoo-2.png", False),
    ("Composição Botânica Fineline", est_fineline, "Agulha 1RL ultrafina com ramificações florais e leveza incomparável.", "images/attila-tattoo-7.jpg", True),
    ("Olho Místico em Pontilhismo", est_blackwork, "Sombreamento ponto a ponto com geometria sagrada e preto puro.", "images/d09ce1b5-67f7-472e-92fd-070f7a3cef81.png", True),
    ("Mandala Floral Sagrada", est_blackwork, "Simetria radial perfeita com encaixe anatômico circular firme.", "images/c7901fe7-f56b-459a-ae6b-626f7e9ed2f9.png", False),
]

for tit, est, desc, img, dest in obras_data:
    Tatuagem.objects.get_or_create(
        titulo=tit,
        defaults={
            "estilo": est,
            "descricao": desc,
            "imagem_url": img,
            "destaque": dest
        }
    )
print(f"[OK] {len(obras_data)} obras registradas na galeria.")

# 7. Orçamento de Exemplo
orc, _ = Orcamento.objects.get_or_create(
    usuario=cliente_user,
    servico=s1,
    defaults={
        "estilo": est_realismo,
        "local_corpo": "Antebraço direito",
        "tamanho_estimado": "15 cm",
        "descricao_ideia": "Gostaria de tatuar um leão com detalhes geométricos na metade do rosto.",
        "status": "aprovado",
        "valor_estimado": 950.00,
        "resposta_estudio": "Projeto excelente! Estimamos 1 sessão de 4 horas. Pronto para agendamento."
    }
)
print("[OK] Orçamento de demonstração registrado.")

# 8. Agendamento (O Movimento)
agd, _ = Agendamento.objects.get_or_create(
    usuario=cliente_user,
    servico=s1,
    data_agendada=date(2026, 10, 20),
    defaults={
        "orcamento": orc,
        "horario": time(14, 0),
        "status": "confirmado",
        "valor_total": 950.00,
        "observacoes_sessao": "Cliente prefere iniciar às 14h. Bancada esterilizada e decalque aprovado previamente.",
        "cuidados_pos_procedimento": "Manter filme plástico por 2 horas, lavar com sabonete neutro e aplicar pomada cicatrizante 3x ao dia."
    }
)
print("[OK] Agendamento (O Movimento) registrado com sucesso.")

print("--- SEEDING CONCLUÍDO COM SUCESSO! ---")
