---
title: "Protocolo y Módulo de Exportación Imprimible con Marca de Agua y Registro Corporativo (Energy CPY)"
type: protocolo-modulo
module_id: "exportacion-imprimible-marca-agua-energycpy"
agente_responsable: "desarrollador-web-showroom"
tags:
  - #protocolo
  - #modulo-exportacion
  - #impresion-a4
  - #marca-de-agua
  - #energy-cpy
  - #tablas-transpuestas
  - #showroom
created: 2026-11-10
updated: 2026-11-10
---

# 🖨️ Módulo Estándar de Exportación Imprimible con Registro de Marca de Agua y Datos de la Empresa (`EnergyCPYPrintExportModule`)

## 1. Objetivo
Establecer un módulo estandarizado, reutilizable y obligatorio para el **Agente 03 (`desarrollador-web-showroom`)** y el **Squad de Agentes** cada vez que se genere o actualice una funcionalidad de **exportación o impresión de información desde una página web** (Resúmenes Ejecutivos *One-Pager*, Catálogos de Cartera, Presentaciones Ejecutivas HTML/PDF o Reportes Técnicos).

---

## 2. Los 4 Pilares Obligatorios del Módulo

### Pilar 1: Registro Oficial de Marca de Agua (`WATERMARK_REGISTRY`)
- **Imagen Oficial**: `logo Energy CPY 4v fondo transparente_.png` (almacenada como `assets/images/logo-energy-cpy-4v-transparente.png` y/o embebida en URI Base64 para portabilidad offline).
- **Transparencia**: **60% de transparencia** (`opacity: 0.40` en CSS).
- **Posicionamiento y Escala**: Centrada exactamente en el medio de la hoja imprimible (`top: 50%; left: 50%; transform: translate(-50%, -50%)`) ocupando el **máximo tamaño que quepa en la hoja** (`width: 94%; height: 90%; object-fit: contain;`).
- **Visibilidad Garantizada**: En modo imprimible (`@media print` y `.print-preview`), todos los contenedores, tarjetas y tablas ubicadas por encima de la marca de agua deben utilizar fondos translúcidos (`background: rgba(255, 255, 255, 0.18)` a `0.25`) para no tapar nunca el logotipo central.

### Pilar 2: Registro Oficial de Datos de la Empresa y Consultores (`COMPANY_REGISTRY`)
- **Marca y División**: **ENERGY CPY — Área Desarrollo Sostenible | Private Investment Advisory & Project Finance**.
- **Dominios Oficiales**:
  - Showroom de Inversiones: `https://inventarioenergycpy.github.io/showroom-energycpy/`
  - Hub Renovable RIGI Llave en Mano: `https://inventarioenergycpy.github.io/hub-renovable-rigi-llave-en-mano/`
- **Consultores Oficiales Registrados (cumpliendo Zero-Email-Exposure en vistas públicas)**:
  1. **Javier Ignacio Diaz** — *Consultor Especialista (Energía Solar, BESS, Minería, Agroindustria & Ingeniería)* — WhatsApp: `+54 9 351 2064791`
  2. **Daniel Gonzalez** — *Consultor Especialista (Petróleo & Gas, Pesca Industrial, Hotelería & Real Estate)* — WhatsApp: `+54 9 2974 23-3028`
- **Pie Legal y Normativo**: Referencia a Ley 27.742 (RIGI), Ley 27.191 (MATER), Resoluciones SE 67/2025, 50/2026 y 155/2026, y cláusula de confidencialidad sujeta a firma de NDA para acceso a Data Room.

### Pilar 3: Contraste Tipográfico Negro sobre Fondo Blanco (`HIGH_CONTRAST_PRINT_TYPOGRAPHY`)
- **Fondo de Hoja**: Blanco puro (`#ffffff`).
- **Fuentes de Letra**: Negro puro (`#000000`) y gris carbón oscuro (`#111827`) con pesos `500` a `800`. Queda prohibido el uso de textos blancos, grises claros o amarillos pálidos en la versión imprimible que puedan confundirse con el fondo blanco.

### Pilar 4: Transposición Automática de Tablas que Exceden el Margen (`TRANSPOSED_PRINT_TABLE_ENGINE`)
- Cuando una tabla o matriz comparativa no entra en el margen horizontal de la hoja a imprimir:
  - **Exclusivamente para la versión imprimible (`@media print` y `.print-preview`)**, se oculta la tabla horizontal ancha (`.screen-only-wide-table`) y se cambia automáticamente a un diseño vertical compuesto por:
    1. **Tablas individuales transpuestas** (cambiando filas por columnas: `Parámetro / Indicador` vs. `Valor Auditado`) para cada oferta o proyecto individual, con `break-inside: avoid`.
    2. **Una Tabla Resumen Comparativa de los Totales** ubicada al final.

---

## 🔗 Referencias Relacionales
- [[00-Dashboard-MOC]]
- [[docs/Agentes/03-Desarrollador-Web-Showroom|Agente 03: Desarrollador Web para Showrooms]]
- [[.agents/skills/desarrollador-web-showroom/SKILL|Skill: desarrollador-web-showroom]]
