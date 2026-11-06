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
- `index.html`: Estructura semántica SPA, selector de usuarios acreditados, modal de Diff Visual e integración con SheetJS.
- `css/`: `main.css`, `components.css` y `responsive.css` (Dark Theme Fintech `#070a12`, acentos dorados, semáforos, modales XL y tablas comparativas de Diff).
- `js/modules/`:
  - `dashboard.js`: KPIs en tiempo real y semáforo de vigencias (🔴 🟡 🟢).
  - `projects.js`: Gestión de cartera con precios base, overprice proyectado y accesos rápidos de plantilla/carga Excel.
  - `deals.js`: Pipeline multi-deal por fondos, checklist gatekeeper y botones de exportación/importación masiva.
  - `brokers.js`: Directorio de interlocutores, control de vencimientos y carga rápida de fondos e inversores.
  - `templateManager.js`: Generador dinámico de plantillas Excel multi-hoja (`.xlsx`) auto-adaptable ante cambios de esquema en el store.
  - `smartImporter.js`: Motor de análisis de Excel/CSV, Diff Visual campo por campo, detección de reemplazos, cargas parciales y rollback con snapshots.
  - `compliance.js`: Matriz interactiva en 3 capas y cláusulas esenciales.
  - `settings.js`: Gestor central de plantillas Excel, subida de archivos, historial de snapshots y copias de seguridad JSON.
- `docs/`: Manual operativo para consultores y matriz legal estratégica.

