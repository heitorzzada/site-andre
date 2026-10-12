/**
 * STUDIO OLIVEIRA - Galeria de Obras e Instalações
 * Portfólio oficial curado por estilos artísticos.
 */

const GALLERY_DATA = [
  // --- REALISMO & COLORIDO ---
  {
    id: 1,
    title: "Venom Hiper-Realista",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-1.jpeg",
    description: "Trabalho hiper-realista com profundidade, texturas orgânicas e contraste cinematográfico."
  },
  {
    id: 2,
    title: "Águia Realista em Sombras",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-2.jpeg",
    description: "Sombreamento preto e cinza com riqueza de penas, luz volumétrica e nitidez anatômica."
  },
  {
    id: 3,
    title: "Rã Tropical Viva",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-3.jpeg",
    description: "Realismo colorido vibrante com pigmentação de saturação pura e efeito de umidade natural."
  },
  {
    id: 4,
    title: "Tigre & Retrato Feminino",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-4.jpeg",
    description: "Composição de dupla exposição unindo força felina e delicadeza facial hiper-realista."
  },
  {
    id: 5,
    title: "Faraó do Egito Antigo",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-5.jpeg",
    description: "Estudo escultórico e histórico com textura de ouro envelhecido e degradê suave."
  },
  {
    id: 6,
    title: "Poseidon Deus dos Mares",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-6.jpeg",
    description: "Escultura clássica transposta para a pele com alto contraste dramático e fluxo anatômico."
  },
  {
    id: 7,
    title: "Olhar Selvagem do Tigre",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-7.jpeg",
    description: "Foco hiper-realista no olhar felino com pelos detalhados fio a fio."
  },
  {
    id: 8,
    title: "Guerreiro Espartano",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-8.jpeg",
    description: "Sombreamento profundo e estética bélica grega com armadura metálica realista."
  },
  {
    id: 9,
    title: "Tigre Feroz em Ataque",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-9.jpeg",
    description: "Dinamismo muscular, expressão facial agressiva e transição de tons cinzas perfeitos."
  },
  {
    id: 10,
    title: "Retrato Guerreira Nativa",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/paulo-tattoo-10.jpeg",
    description: "Expressão humana realista com pintura facial, cocar e iluminação suave."
  },
  {
    id: 11,
    title: "Retrato Feminino Colorido",
    category: "realismo",
    categoryLabel: "Realismo & Colorido",
    image: "assets/images/raffa-tattoo-10.jpeg",
    description: "Paleta rica de tons de pele, brilho nos olhos e contraste refinado."
  },

  // --- GEEK & ANIME ---
  {
    id: 12,
    title: "Goku Black Rosé",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-1.jpeg",
    description: "Linhas fiéis à arte original com degradê magenta brilhante e aura vibrante."
  },
  {
    id: 13,
    title: "Golden Frieza Cósmico",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-2.jpeg",
    description: "Cores metálicas douradas e roxas com iluminação de energia e alto impacto visual."
  },
  {
    id: 14,
    title: "Kenpachi & Yachiru (Bleach)",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-3.jpeg",
    description: "Adaptação de cena clássica com traços de mangá e textura de pintura expressiva."
  },
  {
    id: 15,
    title: "Sailor Moon Realista",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-4.jpeg",
    description: "Fusão sofisticada entre a estética dos animes e iluminação realista de pintura a óleo."
  },
  {
    id: 16,
    title: "Goku vs. Vegeta Clássico",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-5.jpeg",
    description: "Cena épica de confronto dos saiyajins com linhas de ação e colorização vibrante."
  },
  {
    id: 17,
    title: "Kratos - God of War",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-6.jpeg",
    description: "Expressão brutal do guerreiro espartano com detalhes da barba, cinzas e cicatriz vermelha."
  },
  {
    id: 18,
    title: "Rengoku Pilar das Chamas",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-7.jpeg",
    description: "Arte dinâmica de Kimetsu no Yaiba com labaredas flamejantes e fidelidade absoluta."
  },
  {
    id: 19,
    title: "Vegito Blue Saiyajin",
    category: "geek",
    categoryLabel: "Geek & Anime",
    image: "assets/images/raffa-tattoo-8.jpeg",
    description: "Coloração intensa com aura azul de divindade e linhas precisas de contorno."
  },

  // --- ORIENTAL CLÁSSICO ---
  {
    id: 20,
    title: "Dragão Oriental Tradicional",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-1.png",
    description: "Composição tradicional japonesa com escamas precisas, bigodes fluidos e nuvens de fundo."
  },
  {
    id: 21,
    title: "Carpa Koi & Flor de Lótus",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-2.png",
    description: "Símbolo milenar de perseverança com movimento de água e equilíbrio entre preto e cinza."
  },
  {
    id: 22,
    title: "Guerreiro Samurai em Batalha",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-3.png",
    description: "Armadura o-yoroi detalhada, máscara menpo e estética tradicional do período Edo."
  },
  {
    id: 23,
    title: "Máscara Hannya Espiritual",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-4.png",
    description: "Iconografia do teatro Noh com chifres nítidos, expressão poderosa e flores de cerejeira."
  },
  {
    id: 24,
    title: "Tigre & Bambuzal Sagrado",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-5.png",
    description: "Estilo ukiyo-e com anatomia expressiva japonesa e enquadramento dinâmico no corpo."
  },
  {
    id: 25,
    title: "Oni e Chamas do Submundo",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-6.png",
    description: "Fechamento de braço oriental com contraste denso e acabamento refinado de sombras."
  },
  {
    id: 26,
    title: "Serpente Mística & Peônias",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-8.png",
    description: "Fluidez orgânica contornando a musculatura, simbolizando renovação e nobreza."
  },
  {
    id: 27,
    title: "Gueixa e Leque Imperial",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-10.png",
    description: "Delicadeza de traços com quimono ornamentado e sombreamento suave em tons cinzas."
  },
  {
    id: 28,
    title: "Fênix Hou-ou Ascendente",
    category: "oriental",
    categoryLabel: "Oriental Clássico",
    image: "assets/images/attila-tattoo-12.png",
    description: "Cauda plumada longa em curvas elegantes com preenchimento limpo e movimento contínuo."
  },

  // --- FINELINE & DELICADA ---
  {
    id: 29,
    title: "Composição Botânica Fineline",
    category: "fineline",
    categoryLabel: "Fineline & Delicada",
    image: "assets/images/attila-tattoo-7.jpg",
    description: "Agulha 1RL ultrafina com ramificações florais, leveza e elegância atemporal."
  },
  {
    id: 30,
    title: "Constelação & Miniatura Botânica",
    category: "fineline",
    categoryLabel: "Fineline & Delicada",
    image: "assets/images/attila-tattoo-9.png",
    description: "Traços milimétricos com pontilhismo sutil e precisão geométrica harmoniosa."
  },
  {
    id: 31,
    title: "Flor de Lótus Minimalista",
    category: "fineline",
    categoryLabel: "Fineline & Delicada",
    image: "assets/images/attila-tattoo-11.png",
    description: "Linhas puras e simétricas projetadas para valorizar a anatomia com sutileza."
  },
  {
    id: 32,
    title: "Orquídea & Tipografia Caligráfica",
    category: "fineline",
    categoryLabel: "Fineline & Delicada",
    image: "assets/images/attila-tattoo-13.png",
    description: "Encontro entre lettering manual fluido e flores silvestres em traço fino impecável."
  },
  {
    id: 33,
    title: "Micro-Botânica Silvestre",
    category: "fineline",
    categoryLabel: "Fineline & Delicada",
    image: "assets/images/3aefd914-f60c-4d2e-9633-c83f1900b8fa.png",
    description: "Micro-realismo botânico com folhas translúcidas e degradê quase imperceptível."
  },

  // --- BLACKWORK & GEOMÉTRICO ---
  {
    id: 34,
    title: "Olho Místico em Pontilhismo",
    category: "blackwork",
    categoryLabel: "Blackwork & Geométrico",
    image: "assets/images/d09ce1b5-67f7-472e-92fd-070f7a3cef81.png",
    description: "Sombreamento executado ponto a ponto com geometria sagrada e preto puro."
  },
  {
    id: 35,
    title: "Mandala Floral Sagrada",
    category: "blackwork",
    categoryLabel: "Blackwork & Geométrico",
    image: "assets/images/c7901fe7-f56b-459a-ae6b-626f7e9ed2f9.png",
    description: "Simetria radial perfeita com encaixe anatômico circular e linhas firmes e contínuas."
  },
  {
    id: 36,
    title: "Mandala Ornamental Escura",
    category: "blackwork",
    categoryLabel: "Blackwork & Geométrico",
    image: "assets/images/cf035543-5b33-4a33-8ec0-2cdf8c0bb111.png",
    description: "Blackwork sólido combinado com espaços negativos na pele para contraste marcante."
  },
  {
    id: 37,
    title: "Bracelete Geométrico Ornamental",
    category: "blackwork",
    categoryLabel: "Blackwork & Geométrico",
    image: "assets/images/e116c9dc-210a-40a9-aa81-8820207f210c.png",
    description: "Padrão rítmico que contorna o membro em 360 graus com alinhamento milimétrico."
  },
  {
    id: 38,
    title: "Constelação Geométrica & Linhas",
    category: "blackwork",
    categoryLabel: "Blackwork & Geométrico",
    image: "assets/images/9e3ca254-4bf9-4f1c-ba4c-68db9894eb76.png",
    description: "Intersecções retilíneas, esferas e gradientes pontilhados modernos."
  },
  {
    id: 39,
    title: "Composição Blackwork Autoral",
    category: "blackwork",
    categoryLabel: "Blackwork & Geométrico",
    image: "assets/images/6e1657a4-7bba-4bdd-9f33-a7e5573602a1.png",
    description: "Arte conceitual sombria com preenchimento negro profundo e texturas hachuradas."
  }
];

const STUDIO_SPACES = [
  {
    id: "space-1",
    title: "Recepção & Lounge de Entrada",
    subtitle: "Atendimento acolhedor e exclusivo no coração de Moema",
    image: "assets/images/992cd6c5-5939-4eb1-9173-1e98744b2961.png",
    description: "Ambiente sofisticado com iluminação personalizada, cafeteria e área de espera reservada."
  },
  {
    id: "space-2",
    title: "Salão Principal de Procedimentos",
    subtitle: "Amplitude, iluminação cirúrgica e climatização controlada",
    image: "assets/images/fc86e49e-c81d-422d-b7ee-a3d03f2cdfd8.png",
    description: "Estações de trabalho com layout aberto e ergonômico, mantendo distância e privacidade."
  },
  {
    id: "space-3",
    title: "Estação Individual Esterilizada",
    subtitle: "Rigidez hospitalar e 100% materiais descartáveis",
    image: "assets/images/3bea76d9-d397-4724-ba5d-312b4f8493a1.png",
    description: "Bancadas cirúrgicas em aço inoxidável com barreira plástica estéril e biossegurança máxima."
  },
  {
    id: "space-4",
    title: "Área de Criação & Arte",
    subtitle: "Espaço dedicado ao desenho e personalização de projetos",
    image: "assets/images/b1963cf0-15f1-43e2-9b1c-f9805c2bf130.png",
    description: "Mesas de luz digitais e acervo de referências para desenvolvimento de peças sob medida."
  },
  {
    id: "space-5",
    title: "Lounge de Convivência & Conforto",
    subtitle: "Estrutura completa para acompanhantes e momentos de pausa",
    image: "assets/images/0193441e-8e26-45c7-bcaa-1b368286bbf3.png",
    description: "Poltronas anatômicas, Wi-Fi de alta velocidade e ambientação sonora acústica."
  },
  {
    id: "space-6",
    title: "Consultório de Procedimentos Especiais",
    subtitle: "Privacidade absoluta para laser, piercings e estética",
    image: "assets/images/7fc48555-5fd3-4efb-ba9c-42799072308e.png",
    description: "Sala isolada com maca hospitalar elétrica para remoção a laser e estética reparadora."
  }
];
