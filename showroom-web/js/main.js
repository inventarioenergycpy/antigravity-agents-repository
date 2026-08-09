/* ==========================================================================
   JavaScript Principal - Showroom de Inversiones (Inventario Energy CPY)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    initFilters();
    initAnimatedStats();
});

// --- Filtrado de Proyectos por Categoría ---
function initFilters() {
    const filterButtons = document.querySelectorAll('.tab-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filterValue === 'all' || category === filterValue) {
                    card.style.display = 'block';
                    card.style.opacity = '1';
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                }
            });
        });
    });
}

// --- Contadores Animados de Métricas ---
function initAnimatedStats() {
    const statNumbers = document.querySelectorAll('.stat-number');
    let animated = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animated) {
                statNumbers.forEach(stat => {
                    const target = parseFloat(stat.getAttribute('data-target'));
                    const isPercentage = stat.innerText.includes('%');
                    const isCurrency = stat.innerText.includes('M+');
                    
                    let current = 0;
                    const duration = 1500;
                    const stepTime = 30;
                    const steps = duration / stepTime;
                    const increment = target / steps;

                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            current = target;
                            clearInterval(timer);
                        }

                        if (isPercentage) {
                            stat.innerText = current.toFixed(1) + '%';
                        } else if (isCurrency) {
                            stat.innerText = '$' + Math.floor(current) + 'M+';
                        } else {
                            stat.innerText = Math.floor(current);
                        }
                    }, stepTime);
                });
                animated = true;
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        observer.observe(statsSection);
    }
}

// --- Modales ---
function openModal(projectName) {
    const modal = document.getElementById('contactModal');
    const title = document.getElementById('modalTitle');
    if (title) title.innerText = `Dossier: ${projectName}`;
    if (modal) modal.classList.add('active');
}

function closeModal() {
    const modal = document.getElementById('contactModal');
    if (modal) modal.classList.remove('active');
}

function openStyleModal() {
    const modal = document.getElementById('styleModal');
    if (modal) modal.classList.add('active');
}

function closeStyleModal() {
    const modal = document.getElementById('styleModal');
    if (modal) modal.classList.remove('active');
}

function handleFormSubmit(e) {
    e.preventDefault();
    alert('¡Gracias por su interés! El dossier financiero ha sido enviado a la carpeta de descargas del agente.');
    closeModal();
}
