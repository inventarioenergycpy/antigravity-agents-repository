---
title: "Proyecto: PROTELEM - Indicadores Gerencia Comercial (Documentación & Arquitectura Semántica)"
type: proyecto
agente: "ciencia-de-datos"
tags:
  - #proyecto
  - #powerbi
  - #pbip
  - #tmdl
  - #fabric
  - #directquery
  - #protelem
  - #epec
created: 2026-08-20
---

# 📊 Ficha de Proyecto: PROTELEM - Indicadores Gerencia Comercial

- **Identificador del Proyecto**: `protelem-indicadores-gerencia-comercial`
- **Agente Responsable**: `ciencia-de-datos`
- **Fecha de Desarrollo**: 2026-08-20
- **Repositorio Dedicado**: `https://github.com/inventarioenergycpy/protelem-indicadores-gerencia-comercial.git`
- **Ruta Local del Repositorio**: `C:\Users\jidiaz\.gemini\antigravity-ide\scratch\protelem-indicadores-gerencia-comercial`
- **Copia Local del Informe en Descargas**: `D:\Usuarios\jidiaz\Downloads\PROTELEM_Indicadores_Gerencia_Comercial_Informe_Tecnico.md`

---

## 🎯 Objetivo y Alcance

Realizar la ingeniería inversa completa, auditoría arquitectónica y documentación exhaustiva de capacidades del modelo semántico y reporte Power BI Project (`.pbip`) de la Gerencia Comercial de EPEC (**PROTELEM**), siguiendo el formato y estándar del documento de referencia `Ordenativos_Todas_Zona_Informe (1).pdf`.

---

## 🏗️ Resumen Arquitectónico

1. **Orígenes de Datos**:
   - **Microsoft Fabric Data Warehouse (DirectQuery SQL)**: 3 endpoints analíticos (`WH_FACTURACION`, `DW_INDICADORES`, `datos_generales`).
   - **SharePoint Online (Import)**: Metas gerenciales y saldos de mora desde `Objetivos_Indicadores_Comercial.xlsx`.
2. **Esquema Relacional**:
   - Fact-Constellation Schema unificado mediante **claves sintéticas compuestas** (`KEY_ZON_LOC_SCF`, `KEY_TAR_CLA_TEN_TC_TG`, `KEY_ZON_PLAN_R_RF_GF`) contra dimensiones maestras `sigec_idx_*`.
3. **Lógica Temporal y Auditoría**:
   - Desfases en el calendario maestro (`Año#Mes (-1)` y `Año#Mes (-2)`) para alinear ciclos contables cerrados de facturación y toma de estados.
4. **Métricas y Visualización**:
   - +200 medidas DAX estructuradas en 5 dominios de negocio (Facturación, Ilícitos, Mora por tarifas T1 a TS, Tiempos de Ejecución y Atención al Cliente).
   - Capa de presentación Cockpit con **36 tacómetros (gauges) tricolor** con semáforos y límites dinámicos.

---

## 🔗 Referencias Relacionales
- [[00-Dashboard-MOC]]
- [[docs/Historial-Mejoras/2026-08-20_ciencia-de-datos_ingenieria-inversa-pbip-tmdl|Mejora Continua: Ingeniería Inversa PBIP TMDL]]
- [[docs/Agentes/02-Ciencia-de-Datos|Ficha Técnica del Agente de Ciencia de Datos]]
