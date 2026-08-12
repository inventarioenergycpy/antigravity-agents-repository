/* ==========================================================================
   Main JavaScript Logic — Energy CPY Investment Showroom
   ========================================================================== */

// Official Representative Contact Information
const OFFICIAL_CONTACT = {
    name: "Diaz Javier Ignacio",
    email: "areasostenible.consultorespyme@gmail.com",
    phone: "+54 9 351 2064791",
    whatsappLink: "https://wa.me/5493512064791"
};

// Project Database with Slide Images & Detailed Technical Data
const PROJECTS_DATA = {
    "solar": {
        id: "solar",
        categoryTag: "Energía Solar Fotovoltaica",
        title: "Plantas Solares Fotovoltaicas Llave en Mano",
        location: "Regiones Cuyo y NOA, Argentina",
        status: "Co-Financiado 50% CAPEX",
        pdfPath: "assets/docs/plantas_solares_2026.pdf",
        totalSlides: 13,
        slidePrefix: "assets/slides/Inversión_en_Plantas_Solares_en_Argentina_2026_page_",
        description: "Desarrollo estratégico de parques fotovoltaicos llave en mano con el 50% del CAPEX pre-financiado por fabricante global de primer nivel. Estructuración de venta de energía a largo plazo (15 a 20 años) en el mercado MATER / CAMMESA con tarifa indexada al USD.",
        highlights: [
            "50% del CAPEX pre-financiado directamente por el fabricante de paneles e inversores.",
            "Contratos PPA indexados al Dólar estadounidense a 15-20 años de plazo.",
            "Recurso solar excepcional en Cuyo y NOA con factor de capacidad líder global.",
            "Contrato EPC llave en mano con cronogramas y costos cerrados y garantizados.",
            "Garantía de rendimiento y mantenimiento preventivo bajo contratos de O&M."
        ],
        metrics: [
            { label: "Co-Financiamiento", val: "50% CAPEX", color: "text-gold" },
            { label: "Plazo PPA", val: "15 - 20 Años USD", color: "text-cyan" },
            { label: "Mercado Objetivo", val: "MATER / CAMMESA", color: "text-green" },
            { label: "Modalidad", val: "EPC Llave en Mano", color: "text-gold" }
        ]
    },

    "pesca-gran-escala": {
        id: "pesca-gran-escala",
        categoryTag: "Pesca Industrial Gran Escala",
        title: "Proyecto 6.6 — Pesca Industrial de Gran Escala en Patagonia",
        location: "Zona Económica Exclusiva (ZEE) Argentina",
        status: "USD 260M CAPEX",
        pdfPath: "assets/docs/pesca_industrial_2026.pdf",
        totalSlides: 13,
        slidePrefix: "assets/slides/Proyectos_de_Pesca_Industrial_en_Argentina_2026_page_",
        description: "Un modelo industrial robusto y consolidado para capturar la alta rentabilidad de los recursos marinos de exportación en aguas patagónicas. Flota activa de 16 buques altamente equipados y planta propia de congelado e industrialización.",
        highlights: [
            "USD 260 Millones en CAPEX requerido para operación a gran escala.",
            "USD 600 Millones/año en ganancia anual proyectada por capturas de alto valor.",
            "Flota activa de 16 buques de gran calado para Merluza Hubbsi y Langostino Rojo.",
            "Planta terrestre propia de congelado e industrialización de empaque.",
            "Track record comprobado con más de 25 años de operabilidad exitosa."
        ],
        metrics: [
            { label: "CAPEX Requerido", val: "USD 260M", color: "text-gold" },
            { label: "Ganancia Anual", val: "USD 600M/año", color: "text-green" },
            { label: "Flota Activa", val: "16 Buques", color: "text-cyan" },
            { label: "Track Record", val: "+25 Años", color: "text-gold" }
        ]
    },

    "pesca-integrado": {
        id: "pesca-integrado",
        categoryTag: "Cadena de Valor Pesquera",
        title: "Proyecto 6.7 — Ecosistema Pesquero Integrado Patagonia",
        location: "Puerto Madryn / Puerto Deseado / Mar del Plata",
        status: "USD 5.5M CAPEX",
        pdfPath: "assets/docs/pesca_industrial_2026.pdf",
        totalSlides: 13,
        slidePrefix: "assets/slides/Proyectos_de_Pesca_Industrial_en_Argentina_2026_page_",
        description: "Estructura de inversión ágil en la cadena de valor pesquera con rápida recuperación de capital (ROI). Integra flota extractiva, procesado rápido en plantas terrestres patagónicas, logística de frío exportable y certificación global MSC Certified.",
        highlights: [
            "CAPEX total optimizado de USD 5.5M con retorno anual proyectado de USD 4.5M.",
            "Asignación presupuestaria: Flota (USD 1.8M), Planta (USD 1.6M), Frío (USD 1.7M), Certificación (USD 0.4M).",
            "Operaciones internacionales reguladas y pesquerías bajo el estándar global MSC Certified.",
            "Demanda inelástica y operaciones 100% dolarizadas de exportación directa a Asia y Europa.",
            "Acceso directo a infraestructura portuaria operacional en Chubut, Santa Cruz y Buenos Aires."
        ],
        metrics: [
            { label: "CAPEX Total", val: "USD 5.5M", color: "text-gold" },
            { label: "Retorno Anual", val: "USD 4.5M/año", color: "text-green" },
            { label: "Certificación", val: "MSC Certified", color: "text-cyan" },
            { label: "Mercados", val: "Asia & Europa USD", color: "text-gold" }
        ]
    },

    "pozo-salta": {
        id: "pozo-salta",
        categoryTag: "Servicios Energéticos & Infraestructura",
        title: "Proyecto Pozo Salta — Infraestructura & Secado de Cuttings",
        location: "Provincia de Salta, Argentina (NOA)",
        status: "Infraestructura Crítica",
        pdfPath: "assets/docs/pozo_salta_2026.pdf",
        totalSlides: 25,
        slidePrefix: "assets/slides/Proyecto_Pozo_Salta___Argentina__2026_page_",
        description: "Proyecto especializado de infraestructura técnica para servicios petroleros y gasíferos en la Cuenca Noroeste. Incluye tratamiento ambiental, secado de cuttings, servicios de locación seca e industrialización de residuos de perforación.",
        highlights: [
            "Dossier técnico extenso de 25 diapositivas con ingeniería de detalle y tratamiento.",
            "Operatividad estratégica en la provincia de Salta (Cuenca Noroeste Argentina).",
            "Tecnología de última generación para secado de cuttings y locación seca ambiental.",
            "Flujo de ingresos en USD respaldado por contratos de servicios a operadoras principales.",
            "Estructura modular escalable para expansión de capacidad operativa."
        ],
        metrics: [
            { label: "Ubicación", val: "Salta (Cuenca NOA)", color: "text-cyan" },
            { label: "Dossier Técnico", val: "25 Diapositivas", color: "text-gold" },
            { label: "Servicios", val: "Secado de Cuttings", color: "text-green" },
            { label: "Mercado", val: "Oil & Gas USD", color: "text-gold" }
        ]
    },

    "reit-strategy": {
        id: "reit-strategy",
        categoryTag: "Fondo de Inversión REIT",
        title: "ENERGY CPY Argentina REIT Investment Strategy 2026",
        location: "Argentina 2026",
        status: "Fondo Dolarizado",
        pdfPath: "assets/docs/reit_strategy_2026.pdf",
        totalSlides: 11,
        slidePrefix: "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        totalSlides: 11,
        slidePrefix: "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        description: "Vehículo REIT (Real Estate Investment Trust) para la adquisición y desarrollo de activos inmobiliarios corporativos e industriales vinculados al sector energético y logístico en Argentina.",
        highlights: [
            "Portafolio diversificado de renta corporativa dolarizada.",
            "Estructuración de fideicomisos financieros respaldados por activos físicos tangibles.",
            "Rendimiento de doble dígito en USD con distribución periódica de utilidades.",
            "Gobernanza transparente y supervisión ejecutiva especializada.",
            "Mitigación de volatilidad mediante contratos corporativos a largo plazo."
        ],
        metrics: [
            { label: "Vehículo", val: "REIT Fund 2026", color: "text-gold" },
            { label: "Presentación", val: "11 Diapositivas", color: "text-cyan" },
            { label: "Moneda", val: "USD Dolarizado", color: "text-green" },
            { label: "Activos", val: "Real Estate & Energy", color: "text-gold" }
        ]
    }
};

// Modal & Slide Viewer State Variables
let currentProjectId = null;
let currentSlideIndex = 1;
let totalSlidesInCurrentProject = 1;

document.addEventListener("DOMContentLoaded", () => {
    initFilterTabs();
    initAnimatedCounters();
    initMobileMenu();
    initKeyboardNavigation();
});

/* --- Filter Tabs Logic --- */
function initFilterTabs() {
    const tabs = document.querySelectorAll("#filterTabs .tab-btn");
    const cards = document.querySelectorAll("#projectsGrid .project-card");

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");

            const filter = tab.getAttribute("data-filter");

            cards.forEach(card => {
                const category = card.getAttribute("data-category");
                if (filter === "all" || category === filter) {
                    card.style.display = "flex";
                } else {
                    card.style.display = "none";
                }
            });
        });
    });
}

/* --- Animated Number Counters --- */
function initAnimatedCounters() {
    const statCards = document.querySelectorAll(".stat-number");
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseFloat(entry.target.getAttribute("data-target"));
                animateValue(entry.target, 0, target, 2000);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statCards.forEach(card => observer.observe(card));
}

function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const val = (progress * (end - start) + start).toFixed(end % 1 === 0 ? 0 : 1);
        
        if (end === 265.5) obj.innerHTML = `USD ${val}M`;
        else if (end === 50) obj.innerHTML = `${val}%`;
        else if (end === 25) obj.innerHTML = `+${val} Años`;
        else if (end === 20) obj.innerHTML = `${val} Años`;
        else obj.innerHTML = val;

        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

/* --- Mobile Menu Toggle --- */
function initMobileMenu() {
    const btn = document.getElementById("mobileMenuBtn");
    const nav = document.getElementById("navLinks");
    
    if (btn && nav) {
        btn.addEventListener("click", () => {
            nav.classList.toggle("mobile-active");
            btn.innerHTML = nav.classList.contains("mobile-active") ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
        });
    }
}

/* --- Modal & Slide Viewer Functions --- */
function openProjectModal(projectId) {
    const project = PROJECTS_DATA[projectId];
    if (!project) return;

    currentProjectId = projectId;
    currentSlideIndex = 1;
    totalSlidesInCurrentProject = project.totalSlides;

    // Set Modal Header & Text
    document.getElementById("modalTag").innerText = project.categoryTag;
    document.getElementById("modalTitle").innerText = project.title;
    document.getElementById("modalDesc").innerText = project.description;

    // Set PDF & WhatsApp Links
    const pdfBtn = document.getElementById("modalPdfBtn");
    pdfBtn.href = project.pdfPath;
    pdfBtn.setAttribute("download", project.title + ".pdf");

    const wspBtn = document.getElementById("modalWspBtn");
    const wspText = encodeURIComponent(`Hola Javier Diaz, solicito la ficha técnica e información detallada del proyecto "${project.title}".`);
    wspBtn.href = `${OFFICIAL_CONTACT.whatsappLink}?text=${wspText}`;

    // Render Highlights
    const highlightsUl = document.getElementById("modalHighlights");
    highlightsUl.innerHTML = project.highlights.map(h => `<li>${h}</li>`).join("");

    // Render Metrics Summary
    const metricsDiv = document.getElementById("modalMetrics");
    metricsDiv.innerHTML = project.metrics.map(m => `
        <div class="stat-card" style="padding: 12px; text-align: center;">
            <span class="metric-val ${m.color}">${m.val}</span>
            <span class="metric-lbl" style="display: block; font-size: 0.75rem;">${m.label}</span>
        </div>
    `).join("");

    // Render Slide Image & Counter
    updateSlideDisplay();

    // Render Thumbnails
    renderThumbnails();

    // Show Modal
    const modal = document.getElementById("projectModal");
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
}

function updateSlideDisplay() {
    const project = PROJECTS_DATA[currentProjectId];
    if (!project) return;

    const img = document.getElementById("modalSlideImg");
    img.src = `${project.slidePrefix}${currentSlideIndex}.png`;

    const counter = document.getElementById("slideCounter");
    counter.innerText = `Diapositiva ${currentSlideIndex} de ${totalSlidesInCurrentProject}`;

    // Highlight active thumbnail
    const thumbs = document.querySelectorAll("#modalThumbnails .slide-thumb");
    thumbs.forEach((t, idx) => {
        if (idx + 1 === currentSlideIndex) {
            t.classList.add("active");
            t.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
        } else {
            t.classList.remove("active");
        }
    });
}

function renderThumbnails() {
    const project = PROJECTS_DATA[currentProjectId];
    const container = document.getElementById("modalThumbnails");
    container.innerHTML = "";

    for (let i = 1; i <= project.totalSlides; i++) {
        const thumb = document.createElement("img");
        thumb.src = `${project.slidePrefix}${i}.png`;
        thumb.alt = `Slide ${i}`;
        thumb.className = `slide-thumb ${i === currentSlideIndex ? 'active' : ''}`;
        thumb.onclick = () => {
            currentSlideIndex = i;
            updateSlideDisplay();
        };
        container.appendChild(thumb);
    }
}

function changeSlide(direction) {
    currentSlideIndex += direction;
    if (currentSlideIndex < 1) {
        currentSlideIndex = totalSlidesInCurrentProject;
    } else if (currentSlideIndex > totalSlidesInCurrentProject) {
        currentSlideIndex = 1;
    }
    updateSlideDisplay();
}

function closeProjectModal() {
    const modal = document.getElementById("projectModal");
    modal.classList.remove("active");
    document.body.style.overflow = "";
}

function closeModalOnBackdrop(event) {
    if (event.target.classList.contains("modal-backdrop")) {
        closeProjectModal();
    }
}

function initKeyboardNavigation() {
    document.addEventListener("keydown", (e) => {
        const modal = document.getElementById("projectModal");
        if (!modal.classList.contains("active")) return;

        if (e.key === "ArrowLeft") {
            changeSlide(-1);
        } else if (e.key === "ArrowRight") {
            changeSlide(1);
        } else if (e.key === "Escape") {
            closeProjectModal();
        }
    });
}

/* --- Contact Form Handler --- */
function handleFormSubmit(event) {
    event.preventDefault();
    
    const name = document.getElementById("formName").value.trim();
    const email = document.getElementById("formEmail").value.trim();
    const phone = document.getElementById("formPhone").value.trim();
    const project = document.getElementById("formProject").value;
    const message = document.getElementById("formMessage").value.trim();

    if (!name || !email || !phone || !project) return;

    // Show Success Message Alert
    document.getElementById("contactForm").style.display = "none";
    document.getElementById("formSuccessMessage").style.display = "flex";

    // Prepare direct mailto backup trigger
    console.log(`Consulta recibida para Javier Diaz (${OFFICIAL_CONTACT.email}):`, { name, email, phone, project, message });
}
