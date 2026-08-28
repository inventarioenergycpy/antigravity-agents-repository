---
type: historial-mejora
agente: "[[docs/Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom]]"
fecha: 2026-08-28
backup_asociado: "[[docs/Backups/2026-08-28_080500_desarrollador-web-showroom_SKILL.md.bak]]"
tags:
  - #historial
  - #mejora
  - #showroom
  - #bilingue
  - #filtros
  - #admin
---

# Registro de Mejora: [Desarrollador Web Showroom] — Actualización Integral del Showroom Energy CPY

## 📝 Descripción del Cambio y Requerimientos
- **Contexto**: Implementación de mejoras estratégicas solicitadas por la dirección de Energy CPY para optimizar la búsqueda de proyectos, la interacción bilingüe con clientes internacionales, el ruteo confidencial de consultas por temática y la administración del estado de avance de los proyectos.
- **Reglas y Funcionalidades Incorporadas**:
  1. **Selector de Idioma Bilingüe (ES 🇦🇷 / EN 🇺🇸)**: Switch dinámico en la barra de navegación con banderas vectoriales y traducción reactiva al 100% de la interfaz (textos, filtros, fichas técnicas, métricas y modales).
  2. **Filtros Avanzados para Clientes e Invitados (Rango Desde - Hasta)**: Filtro interactivo de Monto de Proyecto en USD con campos numéricos *"Desde"* y *"Hasta"*, chips de presets rápidos (`< USD 10M`, `USD 10M - 50M`, `USD 50M - 200M`, `> USD 200M`), selector de categorías y buscador de texto.
  3. **Confidencialidad Absoluta de Correos & Ruteo Silencioso por Temática**:
     - Cero exposición pública de correos electrónicos en el sitio web (solo números de WhatsApp directo para Javier y Daniel).
     - Ruteo automático e interno de consultas por temáticas:
       - **Javier Ignacio Diaz** (`areasostenible.consultorespyme@gmail.com` | `+54 9 351 2064791`): Minería, Energía Renovable, Proyectos de Ingeniería y Proyectos en Inglés.
       - **Daniel Gonzalez** (`gonzalezmarcelo2105ypf@gmail.com` | `+54 9 2974 23-3028`): Hotelería, Pesca, Petróleo, TRUST Real Estate, REIT, Renta Corporativa y Asesoramiento Financiero.
  4. **Panel de Gestión de Estados con Acceso por Correo**: Modal administrativo habilitado tras validar el correo del consultor, permitiendo marcar proyectos como:
     - 🔵 **Activo** (Color Azul)
     - 🟡 **En trámite** (Color Amarillo)
     - 🟢 **Vendido** (Color Verde)
     Con persistencia reactiva en `localStorage`.

## 🛡️ Resguardo / Backup de Seguridad
- Se ha generado el respaldo preventivo en: `[[docs/Backups/2026-08-28_080500_desarrollador-web-showroom_SKILL.md.bak]]`

## 🎯 Impacto y Beneficio
- Proporciona una experiencia de usuario de nivel institucional para inversores nacionales e internacionales, agilizando el descubrimiento de oportunidades y canalizando las consultas de forma ordenada y privada directamente a los consultores responsables.

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[docs/Agentes/03-Desarrollador-Web-Showroom]]
- [[docs/Proyectos/2026-08-14_showroom-energycpy]]
- [Repositorio Remoto Showroom](https://github.com/inventarioenergycpy/showroom-energycpy)
