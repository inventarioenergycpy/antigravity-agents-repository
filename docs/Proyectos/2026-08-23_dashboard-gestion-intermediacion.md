---
type: proyecto
proyecto: "Dashboard de Gestión e Intermediación Financiera"
agente_responsable: "[[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]]"
repositorio_github: "https://github.com/inventarioenergycpy/dashboard-gestion-intermediacion"
despliegue_url: "https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/"
fecha_creacion: 2026-08-23
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
---

# Proyecto: Dashboard de Gestión e Intermediación Financiera

## 🎯 Objetivo y Alcance
Plataforma ejecutiva web tipo Dashboard SPA diseñada para la administración y supervisión de proyectos de inversión, seguimiento de sub-gestiones con Fondos de Inversión / Brokers y aplicación estricta de la **Estrategia Documental de Protección Legal en 3 Capas** (anti-circunvención, overprice, períodos de cola de 12 a 24 meses y trazabilidad fehaciente con cartas de registro *Deal Log*).

## 🔗 Repositorio Dedicado y Despliegue Live
- **Repositorio Dedicado GitHub**: [inventarioenergycpy/dashboard-gestion-intermediacion](https://github.com/inventarioenergycpy/dashboard-gestion-intermediacion)
- **URL Live (GitHub Pages)**: [https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/](https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/)

## 👤 Agente Responsable
- [[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]] (en colaboración con [[docs/Agentes/01-Analista-Financiero|Analista Financiero]])

## 👥 Control de Acceso y Perfiles
- **Javier** (`inventario.energycpy@gmail.com`): Administrador & Consultor.
- **Daniel** (`gonzalezmarcelo2105ypf@gmail.com`): Consultor.

## ⚖️ Núcleo de Protección Legal (3 Capas)
1. **Capa 1 (Confidencialidad & Anti-Circunvención)**: NDA Bilateral con Inversores y NCNDA con Brokers antes de revelar datos sensibles.
2. **Capa 2 (Mandatos & Reparto de Honorarios)**: Mandato de Venta con Overprice y *Tail Period* (Dueño Directo), Co-Brokering (Consultoras) y MFPA (Brokers Externos).
3. **Capa 3 (Registro & Trazabilidad)**: Carta Formal de Registro de Inversores (*Deal Log*), Anexo Económico (*Deal Specific Addendum*) y minutas de seguimiento.

## 📂 Componentes del Proyecto
- `index.html`: Estructura semántica SPA y selector de usuarios acreditados.
- `css/`: `main.css`, `components.css` y `responsive.css` (Dark Theme Fintech `#070a12`, acentos dorados y semáforos).
- `js/modules/`:
  - `dashboard.js`: KPIs en tiempo real y semáforo de vigencias (🔴 🟡 🟢).
  - `projects.js`: Gestión de cartera con precios base y overprice proyectado.
  - `deals.js`: Pipeline multi-deal por fondos y checklist gatekeeper.
  - `brokers.js`: Directorio de interlocutores y control de vencimientos.
  - `compliance.js`: Matriz interactiva en 3 capas y cláusulas esenciales.
  - `settings.js`: Editor de estados de proyectos y copias de seguridad JSON.
- `docs/`: Manual operativo para consultores y matriz legal estratégica.
