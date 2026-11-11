---
type: proyecto
proyecto: "Dashboard de Gestión e Intermediación Financiera"
agente_responsable: "[[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]]"
repositorio_github: "https://github.com/inventarioenergycpy/dashboard-gestion-intermediacion"
despliegue_url: "https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/"
rama_activa_desarrollo: "feat/reingenieria-ui-stitch-design-md"
fecha_creacion: 2026-08-23
fecha_actualizacion: 2026-10-28
usuarios_autorizados:
  - "Javier (inventario.energycpy@gmail.com) - Admin & Consultor"
  - "Daniel (gonzalezmarcelo2105ypf@gmail.com) - Consultor"
tags:
  - #proyecto
  - #dashboard
  - #intermediacion-financiera
  - #anti-circunvencion
  - #overprice
  - #github-pages
  - #google-stitch
  - #design-md
  - #responsive
  - #ux-testing
---

# Proyecto: Dashboard de Gestión e Intermediación Financiera

## 🎯 Objetivo y Alcance
Plataforma ejecutiva web tipo Dashboard SPA diseñada para la administración y supervisión de proyectos de inversión, seguimiento de sub-gestiones con Fondos de Inversión / Brokers, aplicación estricta de la **Estrategia Documental de Protección Legal en 3 Capas** (anti-circunvención, overprice, períodos de cola de 12 a 24 meses y trazabilidad fehaciente con cartas de registro *Deal Log*), y visualización de carteras sincronizadas con el Showroom Web de Inversiones.

---

## 🌐 Repositorio Dedicado y Ramas de Trabajo
- **Repositorio Dedicado GitHub**: [inventarioenergycpy/dashboard-gestion-intermediacion](https://github.com/inventarioenergycpy/dashboard-gestion-intermediacion)
- **URL Live (GitHub Pages)**: [https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/](https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/)
- **Rama Principal Estable**: `master`
- **Rama de Desarrollo Activa (Reingeniería UI)**: `feat/reingenieria-ui-stitch-design-md`
- **Rama de Integración Previa**: `feat/cartera-inversiones-sincronizada`

---

## 🎨 Reingeniería de Interfaz Gráfica con Google Stitch & `DESIGN.md` (2026-10-28)

En octubre de 2026 se completó la reingeniería integral de la interfaz gráfica incorporando los estándares de **Google Stitch (`stitch.withgoogle.com`)**:

1. **Especificación Formal `DESIGN.md`**:
   - Creación del archivo `DESIGN.md` en la raíz del repositorio como Single Source of Truth para tokens de diseño.
   - **Paleta HSL Fintech**: Fondo ultra oscuro (`hsl(222, 47%, 5%)`), superficies glassmorphic (`hsla(220, 40%, 11%, 0.78)`), realces en oro corporativo (`hsl(45, 93%, 47%)`), cian (`hsl(199, 89%, 48%)`) y esmeralda (`hsl(152, 69%, 41%)`).
   - **Tipografía Fluida**: Escala dinámica con `clamp()` para títulos y subtítulos (Outfit + Inter + JetBrains Mono para IDs).
2. **Ergonomía Diferenciada: PC vs. Móviles**:
   - **Modo PC / Desktop ($\ge 1025\text{px}$)**: CSS Grid de 12 columnas (`max-width: 1440px`), micro-interacciones hover a 60 FPS, navegación completa por teclado con `:focus-visible` y modales One-Pager A4.
   - **Modo Móvil / Smartphone ($\le 768\text{px}$)**:
     - **Barra de Navegación Inferior (*Mobile Bottom Bar*)**: Fijada en la zona del pulgar (*Thumb Zone*) con 5 accesos directos (Resumen, Proyectos, Deals, Consultas, Ajustes).
     - **Touch Targets Ergonómicos**: Todos los botones, enlaces e iconos interactivos con tamaño mínimo $\ge 48 \times 48\text{px}$ y separación de $8\text{px}$.
     - **Prevención de Zoom en iOS**: Inputs y selects configurados con `font-size: 16px` para eliminar el auto-zoom forzado de Safari iOS.
     - **Cero Desborde Horizontal**: `html, body { overflow-x: hidden; }` y tablas con scroll horizontal táctil suave (`-webkit-overflow-scrolling: touch;`).

---

## 🏛️ Núcleo de Protección Legal (3 Capas)
1. **Capa 1 (Confidencialidad & Anti-Circunvención)**: NDA Bilateral con Inversores y NCNDA con Brokers antes de revelar datos sensibles.
2. **Capa 2 (Mandatos & Reparto de Honorarios)**: Mandato de Venta con Overprice y *Tail Period* (Dueño Directo), Co-Brokering (Consultoras) y MFPA (Brokers Externos).
3. **Capa 3 (Registro & Trazabilidad)**: Carta Formal de Registro de Inversores (*Deal Log*), Anexo Económico (*Deal Specific Addendum*) y minutas de seguimiento.

---

## 📦 Componentes y Módulos del Proyecto
- `DESIGN.md`: Especificación técnica de tokens visuales y arquitectura responsive.
- `index.html`: SPA semántica con selector de consultores (Javier / Daniel), sidebar desktop y mobile bottom bar.
- `css/`:
  - `main.css`: Variables globales HSL, reset, layout base y foco accesible.
  - `components.css`: Tarjetas glassmorphic, semáforos de vigencia, modales y tablas.
  - `responsive.css`: Breakpoints 480px, 768px, 1024px, 1200px, Thumb Zone y Touch Targets $\ge 48\text{px}$.
- `js/modules/`:
  - `dashboard.js`: KPIs en tiempo real y semáforos de vigencia.
  - `projects.js`: Cartera con precios base, overprice y carga masiva.
  - `deals.js`: Pipeline multi-deal por fondos y checklist gatekeeper.
  - `brokers.js`: Directorio de interlocutores y control de vencimientos.
  - `inquiries.js`: Buzón de consultas y tickets sincronizados con Showroom Web.
  - `templateManager.js` & `smartImporter.js`: Plantillas Excel multi-hoja y Diff Visual con rollback.
  - `compliance.js` & `settings.js`: Matriz legal interactiva y gestor de copias de seguridad.