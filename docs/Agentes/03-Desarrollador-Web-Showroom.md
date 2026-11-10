---
title: "Ficha Técnica: Desarrollador Web para Showrooms, Reportes e Interfaces"
type: agente
agente: "desarrollador-web-showroom"
tags:
  - #agente
  - #desarrollador-web
  - #showroom
  - #google-stitch
  - #design-md
  - #responsive
  - #ux-testing
  - #github-pages
created: 2026-08-09
updated: 2026-11-10
---

# 🎨 Agente 03: Desarrollador Web para Showrooms, Reportes e Interfaces

- **Identificador de Skill**: `desarrollador-web-showroom`
- **Ubicación de Habilidad**: [`.agents/skills/desarrollador-web-showroom/SKILL.md`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/.agents/skills/desarrollador-web-showroom/SKILL.md)
- **Guía Técnica de Referencia**: [`docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md)

---

## 📋 Resumen del Rol
Diseñador, maquetador y desarrollador de sitios web interactivos para showrooms de proyectos de inversión, páginas de reportes técnicos estáticos HTML y web apps. Emplea las mejores prácticas de la industria mediante **Google Stitch (`stitch.withgoogle.com`)**, la especificación **`DESIGN.md`** para tokens de diseño y maquetación pura en **Vanilla CSS moderno adaptativo para computadoras de escritorio y dispositivos móviles**. Incorpora de manera mandatoria el **Rack de Comprobaciones de Integridad de Entregables** para blindar la UI contra fallas de hidratación (`undefined`), datos corruptos en caché local y desincronización entre aplicaciones.

---

## 🚀 Capacidades Principales

1. **Ideación Asistida con Google Stitch & `DESIGN.md`**:
   - Generación Text-to-UI ("Vibe Design") y traducción de requerimientos de negocio a interfaces visuales.
   - Formalización de tokens de diseño en archivos `DESIGN.md` (paletas HSL, tipografías fluidas, escalas de espaciado).
   - Extracción y limpieza a componentes atómicos en Vanilla CSS sin dependencias pesadas.

2. **Ergonomía y Maquetación Diferenciada**:
   - **PC / Desktop**: CSS Grid de 12/24 columnas, micro-interacciones hover a 60 FPS, navegación por teclado y anchos máximos controlados (`max-width: 1400px`).
   - **Dispositivos Móviles**: Enfoque de Zona del Pulgar (*Thumb Zone*), Touch Targets ergonómicos $\ge 48 \times 48\text{px}$, tipografía en inputs $\ge 16\text{px}$ (sin zoom en iOS) y eliminación total de scroll horizontal.

3. **Batería de Pruebas de Validación UX**:
   - **Técnica**: Google Lighthouse $> 90$, Core Web Vitals (LCP $< 2.5\text{s}$, CLS $< 0.1$, INP $< 200\text{ms}$).
   - **Dominio**: Cumplimiento del 100% de la identidad corporativa y ausencia de placeholders.
   - **Accesibilidad**: Certificación WCAG 2.2 AA (contraste $\ge 4.5:1$ y navegación completa por `Tab`).

4. **Rack de Comprobaciones de Integridad de Entregables Web (Zero-Undefined Guardrail)**:
   - **Blindaje contra `undefined`/`null`**: Fallbacks en cascada obligatorios en template literals (`item.title || item.es.title || item.id`).
   - **Dualidad de Esquemas SSOT**: Presencia de propiedades principales tanto en la raíz de objetos JSON como en bloques idiomáticos (`es`/`en`).
   - **Auto-Sanación de Persistencia (`localStorage` Self-Healing)**: Rutinas de detección y reparación reactiva en `loadData()` ante cachés corruptas o desactualizadas en el navegador del cliente.
   - **Sincronización Multicanal**: Mapeo biunívoco de estados y doble canal (`BroadcastChannel` + `window.onstorage`) para ecosistemas sincronizados (Dashboard <---> Showroom).
   - **Pruebas Deterministas Automatizadas**: Ejecución obligatoria de script de validación con salida estricta `Exit Code 0` previa a cualquier `git commit` o despliegue a producción.

---

## 🌐 Plataforma de Despliegue y Trazabilidad
- **Plataforma**: GitHub Pages y repositorios dedicados en `inventarioenergycpy/<proyecto>.git` y `PROTELEM-EPEC/<proyecto>.git`.
- **Trazabilidad**: URLs estables sin backend para consulta y auditoría permanente.

---

## 🔗 Referencias Relacionales
- [[00-Dashboard-MOC]]
- [[docs/Protocolos/Guia-Maestra-Diseno-Web-Google-Stitch-DESIGN-MD|Guía Maestra de Diseño Web con Google Stitch y DESIGN.md]]
- [[docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores|Protocolo Multi-Agente PM y 3 Operadores (Triple QA)]]
- [[docs/Proyectos/README|Índice de Proyectos]]
- [[docs/Backups/README|Bóveda de Backups]]
- [[docs/Historial-Mejoras/README|Historial de Mejoras]]