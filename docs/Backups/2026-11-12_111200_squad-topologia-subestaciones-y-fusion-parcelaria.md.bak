---
title: "Registro de Mejora: Squad Ágil Arquetipo A - Topología de Subestaciones, Fusión Parcelaria y Tarifa Social EPEC"
tags:
  - #historial-mejoras
  - #squad-multi-agente
  - #gis
  - #catastro
  - #subestaciones
  - #tarifa-social
  - #epec
fecha: 2026-11-11
responsable: "Copiloto Orquestador & Squad Ágil PM-Operadores (Arquetipo A)"
repositorio_proyecto: "https://github.com/PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario.git"
---

# 🚀 Registro de Mejora: Topología de Subestaciones, Fusión Parcelaria y Tarifa Social EPEC

## 1. Contexto y Desafío
El relevamiento de cuadrillas comerciales y técnicas de EPEC requería:
1. Una capa unificada y jerárquica de parcelas combinando `parcelas_union`, `municipalidad` e `IDECOR provincial`.
2. El análisis de límites de las 5.296 Subestaciones Transformadoras (`vt_subestaciones_poly`) para detectar parcelas cortadas al medio por la línea perimetral.
3. La clasificación de SETs por volumen de suministros y el mapeo de usuarios bajo Tarifa Social Oficial (Decreto Provincial 43/2019).

---

## 2. Metodología Obligatoria en 6 Etapas

### Fase 1: Investigación en Fuentes Confiables y Verídicas
- Conexión WFS segura a `https://maaysp-ws.cba.gov.ar/EPEC/wfs`.
- Inspección de `EPEC:vt_subestaciones_poly` (5.301 features) y capas parcelarias.
- Auditoría del padrón provincial de 1.208.097 suministros y 94.256 tarifas sociales.

### Fase 2: Diseño Pre-Implementación & Compuerta de Clarificación
- Activación de `copiloto-orquestador-skills`.
- Ranking dinámico Top-2 de modelos Gemini (Top-1 PM: Gemini 2.5 Pro; Top-2 Operadores: Gemini 2.5 Flash).
- Interactive Clarification Gate acordada con el usuario (Ámbito provincial completo, frontera rígida con log de excepciones, Tarifa Social identificada con protocolo especial, y repositorio dedicado `PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario`).

### Fase 3: Diagramación WBS & Contratos Tipados
- Despacho secuencial vía patrón Blackboard en disco (`data/`, `reports/`, `viewer/`).
- WBS-01 (Operador 1 Core GIS): Fusión y saneamiento parcelario.
- WBS-02 (Operador 2 Dominio EPEC): Topología SET y Tarifa Social.
- WBS-03 (Operador 3 QA & UX): Tablero interactivo y verificación Triple QA.

### Fase 4: Presentación de Prueba Piloto
- Validación determinista con exit code 0 en pipelines Python DuckDB / Shapely / GeoPandas.
- Confirmación de 386.005 parcelas saneadas y 110.230 parcelas cortadas.

### Fase 5: Pruebas Integrales & Triple QA
- **QA Técnico**: Cero errores de ejecución, consistencia de tipos, indexación STRtree y GeoJSON válido.
- **QA Dominio**: Conformidad con Decreto Provincial 43/2019 y nomenclatura catastral EPEC.
- **QA Usabilidad**: Tablero interactivo [`viewer/index.html`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/viewer/index.html) con filtros y tablas dinámicas.

### Fase 6: Auto-Documentación, Backup e Historial
- Respaldo preventivo `.bak` en `docs/Backups/2026-11-11_180213_00-Dashboard-MOC.md.bak` y `docs/Backups/2026-11-12_102800_plan-relevamiento-topologia-set-parcelario.md.bak`.
- Nuevo repositorio creado y sincronizado en [PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario](https://github.com/PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario.git).
- Incorporación del informe ejecutivo y dataset por plan de relevamiento (585.819 puntos de Córdoba Capital, 537.633 Clientes Comunes CC y 48.186 otros clientes) en `reports/resumen_plan_relevamiento_clientes_cc_vs_otros.csv` y `docs/04_resumen_puntos_relevamiento_por_plan_cc_vs_otros.md`.

