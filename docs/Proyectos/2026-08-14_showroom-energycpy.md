---
type: proyecto
proyecto: "Showroom Web Energy CPY"
agente_responsable: "[[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]]"
repositorio_github: "https://github.com/inventarioenergycpy/showroom-energycpy"
despliegue_url: "https://inventarioenergycpy.github.io/showroom-energycpy/"
fecha_creacion: 2026-08-14
tags:
  - #proyecto
  - #showroom
  - #github-pages
  - #web
---

# Proyecto: Showroom Web Energy CPY

## 🎯 Objetivo y Alcance
Plataforma ejecutiva web interactiva diseñada para exhibir proyectos de inversión estratégica (Energía Solar MATER, Pesca Industrial en Patagonia, Infraestructura Energética Salta, Minería, Hotelería y Estrategias REIT). Incorpora maquetación Dark Mode / Glassmorphic, selector de idioma bilingüe (ES 🇦🇷 / EN 🇺🇸), catálogo con filtros multicriterio y rango de montos 'Desde - Hasta', ruteo confidencial y silencioso de consultas por correo/WhatsApp a consultores especialistas (Javier Diaz y Daniel Gonzalez), y panel administrativo de gestión de estados de proyectos (Activo 🔵 / En trámite 🟡 / Vendido 🟢).

## 🔗 Repositorio Remoto y Despliegue Live
- **Repositorio Dedicado GitHub**: [inventarioenergycpy/showroom-energycpy](https://github.com/inventarioenergycpy/showroom-energycpy)
- **URL Live (GitHub Pages)**: [https://inventarioenergycpy.github.io/showroom-energycpy/](https://inventarioenergycpy.github.io/showroom-energycpy/)

## 👤 Agente Responsable
- [[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]]

## 📂 Componentes del Proyecto
- `index.html`: Estructura semántica HTML5 con switch bilingüe, barra de filtros avanzados (Desde - Hasta), badges de estados de avance, canal de WhatsApp y modal administrativo protegido.
- `css/styles.css`: Estilos visuales Dark Mode (`#090d16`), tarjetas glassmorphic, estados de color normalizados (Azul `#38bdf8`, Amarillo `#f59e0b`, Verde `#10b981`), dorado corporativo (`#e2b714`) y diseño 100% responsivo.
- `js/main.js`: Motor i18n reactivo (ES/EN), filtrado combinado multicriterio, ruteo silencioso e interno de consultas por temáticas a buzones autorizados (`areasostenible.consultorespyme@gmail.com` / `gonzalezmarcelo2105ypf@gmail.com`), modal interactivo de diapositivas y persistencia de estados en `localStorage`.
- `assets/`: Diapositivas renderizadas (`slides/`), documentos PDF oficiales (`docs/`) e imágenes vectoriales (`images/`).
