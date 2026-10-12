/**
 * STUDIO OLIVEIRA - APP LOGIC & INTERACTIONS
 * Funcionalidades:
 *  - Galeria interativa com filtros de estilos
 *  - Lightbox modal com suporte a teclado (Esc, Setas) e CTA dinâmico
 *  - Renderização dinâmica dos espaços do estúdio
 *  - Menu mobile responsivo e acessível
 *  - Header com efeito scroll e active state por IntersectionObserver
 *  - Formulário inteligente de orçamento com geração direta de WhatsApp oficial
 *  - Tratamento e redirecionamento limpo para rotas antigas (/equipe)
 */

document.addEventListener('DOMContentLoaded', () => {
  // Constantes do Estúdio
  const WHATSAPP_NUMBER = "5511944863323";
  const INSTAGRAM_URL = "https://www.instagram.com/ledstattoo";

  /* ==========================================================================
     1. REDIRECIONAMENTO DE ROTAS ANTIGAS (Ex: #equipe)
     ========================================================================== */
  const currentHash = window.location.hash.toLowerCase();
  const currentPath = window.location.pathname.toLowerCase();
  if (currentHash.includes('equipe') || currentPath.includes('equipe')) {
    window.location.hash = '#galeria';
  }

  /* ==========================================================================
     2. HEADER & NAVEGAÇÃO
     ========================================================================== */
  const header = document.querySelector('.site-header');
  const mobileToggle = document.querySelector('.mobile-nav-toggle');
  const mobileDrawer = document.querySelector('.mobile-nav-drawer');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');
  const navLinks = document.querySelectorAll('.nav-link');

  // Scroll Header Effect
  const handleScroll = () => {
    if (window.scrollY > 40) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // Mobile Menu Toggle
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.toggle('open');
      mobileToggle.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.remove('open');
        mobileToggle.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // Active Link Observer
  const sections = document.querySelectorAll('section[id]');
  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(sec => sectionObserver.observe(sec));

  /* ==========================================================================
     3. GALERIA DE OBRAS & FILTROS
     ========================================================================== */
  const galleryGrid = document.getElementById('galleryGrid');
  const filterButtons = document.querySelectorAll('.filter-btn');

  let currentCategory = 'all';
  let filteredItems = [...GALLERY_DATA];
  let currentLightboxIndex = 0;

  function renderGallery() {
    if (!galleryGrid) return;
    galleryGrid.innerHTML = '';

    filteredItems = currentCategory === 'all'
      ? GALLERY_DATA
      : GALLERY_DATA.filter(item => item.category === currentCategory);

    filteredItems.forEach((item, index) => {
      const card = document.createElement('article');
      card.className = 'gallery-item';
      card.setAttribute('tabindex', '0');
      card.setAttribute('role', 'button');
      card.setAttribute('aria-label', `Ver detalhes de ${item.title}`);

      card.innerHTML = `
        <img class="gallery-img" src="${item.image}" alt="${item.title}" loading="lazy" width="400" height="500">
        <div class="gallery-item-overlay">
          <span class="gallery-item-style">${item.categoryLabel}</span>
          <h3 class="gallery-item-title">${item.title}</h3>
          <span class="gallery-item-cta">
            Ampliar Obra
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </span>
        </div>
      `;

      card.addEventListener('click', () => openLightbox(index));
      card.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openLightbox(index);
        }
      });

      galleryGrid.appendChild(card);
    });
  }

  // Filter Buttons Event
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.getAttribute('data-filter') || 'all';
      renderGallery();
    });
  });

  /* ==========================================================================
     4. LIGHTBOX MODAL
     ========================================================================== */
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxTag = document.getElementById('lightboxTag');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxDesc = document.getElementById('lightboxDesc');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');
  const lightboxQuoteBtn = document.getElementById('lightboxQuoteBtn');

  function openLightbox(index) {
    if (!filteredItems[index] || !lightboxModal) return;
    currentLightboxIndex = index;
    updateLightboxContent();
    lightboxModal.classList.add('active');
    document.body.style.overflow = 'hidden';
    lightboxClose?.focus();
  }

  function closeLightbox() {
    if (!lightboxModal) return;
    lightboxModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function updateLightboxContent() {
    const item = filteredItems[currentLightboxIndex];
    if (!item) return;

    if (lightboxImg) {
      lightboxImg.src = item.image;
      lightboxImg.alt = item.title;
    }
    if (lightboxTag) lightboxTag.textContent = item.categoryLabel;
    if (lightboxTitle) lightboxTitle.textContent = item.title;
    if (lightboxDesc) lightboxDesc.textContent = item.description;

    if (lightboxQuoteBtn) {
      lightboxQuoteBtn.onclick = () => {
        closeLightbox();
        // Pre-fill quote form style
        const styleSelect = document.getElementById('quoteStyle');
        if (styleSelect) {
          styleSelect.value = item.category;
        }
        const descInput = document.getElementById('quoteDescription');
        if (descInput && !descInput.value.includes(item.title)) {
          descInput.value = `Gostei muito da arte "${item.title}" (${item.categoryLabel}) na galeria. Gostaria de um projeto inspirado nesse estilo!`;
        }
        const quoteSection = document.getElementById('orcamento');
        if (quoteSection) {
          quoteSection.scrollIntoView({ behavior: 'smooth' });
        }
      };
    }
  }

  function showNextLightbox() {
    if (filteredItems.length === 0) return;
    currentLightboxIndex = (currentLightboxIndex + 1) % filteredItems.length;
    updateLightboxContent();
  }

  function showPrevLightbox() {
    if (filteredItems.length === 0) return;
    currentLightboxIndex = (currentLightboxIndex - 1 + filteredItems.length) % filteredItems.length;
    updateLightboxContent();
  }

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxNext) lightboxNext.addEventListener('click', showNextLightbox);
  if (lightboxPrev) lightboxPrev.addEventListener('click', showPrevLightbox);

  // Close when clicking modal backdrop
  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) closeLightbox();
    });
  }

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (!lightboxModal || !lightboxModal.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') showNextLightbox();
    if (e.key === 'ArrowLeft') showPrevLightbox();
  });

  /* ==========================================================================
     5. RENDERIZAÇÃO DOS ESPAÇOS DO ESTÚDIO
     ========================================================================== */
  const spacesGrid = document.getElementById('spacesGrid');
  if (spacesGrid && typeof STUDIO_SPACES !== 'undefined') {
    spacesGrid.innerHTML = '';
    STUDIO_SPACES.forEach(space => {
      const card = document.createElement('div');
      card.className = 'space-card';
      card.innerHTML = `
        <div class="space-image-wrapper">
          <img class="space-img" src="${space.image}" alt="${space.title}" loading="lazy" width="400" height="240">
        </div>
        <div class="space-card-body">
          <span class="space-card-subtitle">${space.subtitle}</span>
          <h3 class="space-card-title">${space.title}</h3>
          <p class="space-card-desc">${space.description}</p>
        </div>
      `;
      spacesGrid.appendChild(card);
    });
  }

  /* ==========================================================================
     6. FORMULÁRIO DE ORÇAMENTO (WHATSAPP DEEP LINK)
     ========================================================================== */
  const quoteForm = document.getElementById('quoteForm');
  const quotePhone = document.getElementById('quotePhone');
  const quoteFileInput = document.getElementById('quoteFile');
  const fileDropzone = document.getElementById('fileDropzone');
  const filePreview = document.getElementById('filePreview');
  const filePreviewName = document.getElementById('filePreviewName');
  const formFeedback = document.getElementById('formFeedback');

  // Máscara de Telefone BR
  if (quotePhone) {
    quotePhone.addEventListener('input', (e) => {
      let val = e.target.value.replace(/\D/g, '');
      if (val.length > 11) val = val.substring(0, 11);
      if (val.length > 10) {
        val = val.replace(/^(\d{2})(\d{5})(\d{4})$/, '($1) $2-$3');
      } else if (val.length > 5) {
        val = val.replace(/^(\d{2})(\d{4})(\d{0,4})$/, '($1) $2-$3');
      } else if (val.length > 2) {
        val = val.replace(/^(\d{2})(\d{0,5})$/, '($1) $2');
      }
      e.target.value = val;
    });
  }

  // Upload e Dropzone de Referência
  if (fileDropzone && quoteFileInput) {
    fileDropzone.addEventListener('click', () => quoteFileInput.click());

    ['dragenter', 'dragover'].forEach(eventName => {
      fileDropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        fileDropzone.classList.add('dragover');
      });
    });

    ['dragleave', 'drop'].forEach(eventName => {
      fileDropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        fileDropzone.classList.remove('dragover');
      });
    });

    fileDropzone.addEventListener('drop', (e) => {
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {
        quoteFileInput.files = e.dataTransfer.files;
        handleFileSelect(quoteFileInput.files[0]);
      }
    });

    quoteFileInput.addEventListener('change', () => {
      if (quoteFileInput.files && quoteFileInput.files[0]) {
        handleFileSelect(quoteFileInput.files[0]);
      }
    });
  }

  function handleFileSelect(file) {
    if (!filePreview || !filePreviewName) return;
    filePreviewName.textContent = `${file.name} (${(file.size / 1024).toFixed(1)} KB)`;
    filePreview.classList.add('has-file');
  }

  // Submissão do Formulário
  if (quoteForm) {
    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('quoteName')?.value.trim();
      const phone = quotePhone?.value.trim();
      const service = document.getElementById('quoteService')?.value;
      const style = document.getElementById('quoteStyle')?.value;
      const placement = document.getElementById('quotePlacement')?.value.trim();
      const size = document.getElementById('quoteSize')?.value;
      const description = document.getElementById('quoteDescription')?.value.trim();
      const file = quoteFileInput?.files?.[0];

      if (!name || !phone) {
        showFeedback('Por favor, informe seu nome e WhatsApp para contato.', 'error');
        return;
      }

      // Montagem da mensagem estruturada
      let message = `*SOLICITAÇÃO DE ORÇAMENTO — STUDIO OLIVEIRA*\n\n`;
      message += `*Cliente:* ${name}\n`;
      message += `*WhatsApp:* ${phone}\n`;
      if (service) message += `*Serviço:* ${service}\n`;
      if (style) message += `*Estilo:* ${style}\n`;
      if (placement) message += `*Local do corpo:* ${placement}\n`;
      if (size) message += `*Tamanho estimado:* ${size}\n`;
      if (description) message += `*Descrição da ideia:* ${description}\n`;
      if (file) {
        message += `*Referência:* Possuo o arquivo "${file.name}" para enviar aqui na conversa.\n`;
      }
      message += `\n_Mensagem enviada pelo site oficial do Studio Oliveira._`;

      const whatsappUrl = `https://api.whatsapp.com/send?phone=${WHATSAPP_NUMBER}&text=${encodeURIComponent(message)}`;

      showFeedback('Redirecionando para o WhatsApp oficial do Studio Oliveira...', 'success');

      setTimeout(() => {
        window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
      }, 700);
    });
  }

  function showFeedback(text, type) {
    if (!formFeedback) return;
    formFeedback.textContent = text;
    formFeedback.className = `form-feedback ${type}`;
    formFeedback.style.display = 'flex';
  }

  /* ==========================================================================
     7. BOTÃO FLUTUANTE DE WHATSAPP
     ========================================================================== */
  const floatingWhatsapp = document.getElementById('floatingWhatsapp');
  if (floatingWhatsapp) {
    floatingWhatsapp.addEventListener('click', (e) => {
      e.preventDefault();
      const defaultMsg = "Olá! Gostaria de solicitar um orçamento no Studio Oliveira.";
      const url = `https://api.whatsapp.com/send?phone=${WHATSAPP_NUMBER}&text=${encodeURIComponent(defaultMsg)}`;
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }

  // Inicialização
  renderGallery();
});
