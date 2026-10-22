---
title: "Mejora Continua: Unificación Proyecto Pozo Salta, Exclusión de Avex, Gating de Presentaciones en 5 Proyectos y Resumen Ejecutivo con TIR y Tendencia de Mercado"
fecha: 2026-10-22
agentes:
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
  - "[[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]]"
  - "[[docs/Agentes/01-Analista-Financiero|Analista Financiero]]"
repositorio: "https://github.com/inventarioenergycpy/showroom-energycpy"
rama: "feat/cartera-inversiones-sincronizada"
commit: "59acb55"
tags:
  - #historial-mejora
  - #showroom
  - #pozo-salta
  - #presentaciones
  - #onepager
  - #tendencia-mercado
---

# 🚀 Registro de Mejora Continua: Actualización Integral del Catálogo Showroom Energy CPY

- **Fecha**: 2026-10-22
- **Agentes Involucrados**:
  - Agente 11: Copiloto Orquestador y Selector Dinámico de Habilidades (`copiloto-orquestador-skills`)
  - Agente 03: Desarrollador Web Showroom e Interfaces (`desarrollador-web-showroom`)
  - Agente 01: Analista Financiero & Modelador Económico (`analista-financiero`)
- **Repositorio Modificado**:
  - `showroom-energycpy` (rama `feat/cartera-inversiones-sincronizada`, Commit `59acb55`)

---

## 🎯 1. Requerimientos Implementados

### A. Unificación Estratégica de Proyectos en Salta
- Se unificaron **"Proyecto Pozo Salta — Infraestructura & Secado de Cuttings"** y **"Proyecto Salta - GARRIDO (25 Áreas de Explotación)"** en una sola propuesta consolidada de gran escala:
  - **Título Oficial**: `Proyecto Pozo Salta — Infraestructura & Secado de Cuttings`
  - **Ticket y Monto**: `USD 15M CAPEX Planta / Plan USD 1.870M (25 Áreas)` (Total Cartera: USD 1.885M)
  - **Modalidad**: `Socio Inversor / Concesión & UTE`
  - **Retorno & TIR**: `ROI: 3 Años (Planta) / 20 Años (Concesión) | TIR: 31.0%`
  - **Diapositivas**: 25 diapositivas completas vinculadas a `assets/slides/Proyecto_Pozo_Salta___Argentina__2026_page_` (1 a 25) con portada HD y PDF técnico en `assets/docs/pozo_salta_2026.pdf`.

### B. Remoción de Proyecto Avex
- Se excluyó del catálogo público del showroom el proyecto **"Planta Avícola + Red de Distribución Nacional (Avex)"** (`planta-avicola-avex`), eliminando sus registros de `data/projects-master.json`, `js/main.js` y opciones del selector de contacto en `index.html`.
- El total de proyectos activos en catálogo se ajustó a **24 proyectos** estructurados por un volumen consolidado de **USD 4.111,5 Millones** (+4.1B USD).

### C. Gating Selectivo del Botón "Ver Presentación" (Exactamente 5 Proyectos)
Se programó la restricción estricta (`PRESENTATION_ENABLED_IDS`) en la grilla para que el botón **"Ver Presentación"** se habilite **exclusivamente** para los 5 proyectos que cuentan con presentaciones y diapositivas de alta definición:
1. `Plantas Solares Llave en Mano con Financiamiento Asegurado` (`solar`, 13 diapositivas).
2. `Proyecto Pozo Salta — Infraestructura & Secado de Cuttings` (`pozo-salta`, 25 diapositivas).
3. `ENERGY CPY Argentina REIT Investment Strategy 2026` (`reit-strategy`, 11 diapositivas).
4. `Proyecto 6.6 — Pesca Industrial de Gran Escala en Patagonia` (`pesca-gran-escala`, 13 diapositivas).
5. `Proyecto 6.7 — Ecosistema Pesquero Integrado Patagonia` (`pesca-integrado`, 13 diapositivas).

Para los 19 proyectos restantes, la tarjeta muestra **únicamente** la acción directa a ancho completo **"Resumen Ejecutivo (1 Pág)"** (`.btn-card-op-full`), eliminando botones muertos o diapositivas genéricas.

### D. Enriquecimiento del Resumen Ejecutivo en Todos los Proyectos
En los 24 proyectos del portafolio se incorporaron de manera estructurada (en tarjeta y en el One-Pager A4):
- **Actividad / Sector Industrial**: Tag oficial de categorización en cabecera.
- **Monto de Inversión**: Ticket exacto en USD (con etiqueta confidencial para Private Placement en hoteles boutique).
- **Tipo de Oferta**: Badge visible de `Venta`, `Socio Inversor` o `Venta / Socio Inversor`.
- **Datos de Retorno**: ROI (Años de recupero) y TIR estimada (%) en tarjeta y en Deal Terms Bar.
- **Tendencia del Mercado Local e Internacional**:
  - Sección visual dedicada en el One-Pager (`.op-market-trend-container`) con dos paneles contrastados:
    - *Mercado Local (Argentina)*: Drivers macroeconómicos, PPA MATER, desregulación de exportaciones, RIGI y demanda insatisfecha.
    - *Mercado Internacional*: Demanda global de commodities, precios récord de crudo dulce, gas, oro, litio y proteínas marinas salvajes.
  - Micro-snippet en cada tarjeta del catálogo con ícono de tendencia (`<i class="fa-solid fa-chart-line"></i>`).

---


### E. Portada Institucional (Logo EnergyCPY sobre Fondo Blanco)
- Para evitar previews confusas o recortes de diapositivas prestadas en los **19 proyectos sin presentación interactiva**, se actualizó su imagen de portada (`coverImage`):
  - **Activo Oficial**: [`assets/images/logo_energy_cpy_cover_white.png`](file:///D:/Proyectos/showroom-energycpy/assets/images/logo_energy_cpy_cover_white.png) y [`assets/images/logo_energy_cpy_white.png`](file:///D:/Proyectos/showroom-energycpy/assets/images/logo_energy_cpy_white.png).
  - **Diseño & Encuadre**: Formato canvas de 800x440 px con fondo blanco puro (`#ffffff`), logo circular EnergyCPY *"Área desarrollo sostenible"* centrado y protegido por un degradé superior sutil (`.has-white-bg`) para garantizar legibilidad óptima de tags y badges.
  - **Commit Asociado**: `7dcb865 feat(showroom): actualizar imagen previa con logo EnergyCPY fondo blanco para proyectos sin presentacion`.

## 🧪 2. Validación Automatizada y Verificación

1. **Suite de Pruebas Automatizadas (`validate_showroom.py`)**:
   - Total proyectos: 24 (100% OK).
   - Avex ausente: Verificado.
   - Garrido ausente / unificado en Pozo Salta: Verificado.
   - Pozo Salta con 25 slides: Verificado.
   - 5 proyectos con presentación autorizada: Verificado.
   - Campos `dealType`, `amountUSD`, `roi`, `tir`, `marketTrend` en los 24 proyectos: Verificado (100% OK).
2. **Prueba de Servidor HTTP y Carga de Recursos**:
   - `index.html` (200 OK)
   - `js/main.js` (200 OK)
   - `css/styles.css` (200 OK)
   - `data/projects-master.json` (200 OK)
