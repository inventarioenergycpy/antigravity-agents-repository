---
title: "Registro de Mejora: Recomposición de Manzanas de Alta Resolución por Disolución Parcelaria e Ingesta Incremental WFS (Sprint 1)"
tags:
  - #historial-mejoras
  - #sprint-1
  - #gis
  - #catastro
  - #parcelas-calles
  - #disolucion-topologica
  - #arquetipo-a
date: 2026-10-25
author: Squad Arquetipo A & Project Manager (Gemini 3.8 Flash High)
---

# 📜 Registro de Mejora: Recomposición de Manzanas de Alta Resolución por Disolución Parcelaria e Ingesta WFS (Sprint 1)

- **Fecha**: 25 de Octubre de 2026
- **Sprint**: Sprint 1 — Arquetipo A (GIS, Catastro & Rutas EPEC)
- **Squad Ágil**: PM (*Gemini 3.8 Flash High*) & 3 Operadores (*Gemini 3.7 Flash High*)
- **Estado**: ✅ CONSOLIDADO, VALIDADO Y DESPLEGADO

---

## 1. Contexto y Justificación del Vector Bottom-Up

En la infraestructura cartográfica anterior (IDECOR / WFS macro), la geometría de las manzanas correspondía a polígonos envolventes generales que en zonas rurales o periurbanas abarcaban cientos de hectáreas de campo abierto, obligando a generar buffers artificiales para no superponer macro-triángulos sobre la trama de la ciudad.

Para alcanzar **máxima resolución y fidelidad submétrica**, se implementó el **Vector de Acercamiento Bottom-Up**:
- Partir del átomo indivisible del catastro provincial: la **parcela catastral individual** provista por la capa oficial de GeoServer `EPEC:vm_vt_parcelas_calles`.
- Disolver las parcelas componentes de cada manzana mediante el operador topológico exacto `shapely.ops.unary_union` sobre el sistema de coordenadas métricas planas **POSGAR 94 / Argentina 4 (EPSG:22174)**.
- Reproyectar las geometrías resultantes a **WGS 84 (EPSG:4326)** para su explotación cartográfica web.

---

## 2. Implementación Técnica y Entregables del Sprint 1

### A. Pipeline de Ingesta Incremental con Caché Local
- **Script Rector**: [`scripts/pipeline_sprint1_parcelas_manzanas_alta_resolucion.py`](file:///D:/Proyectos/antigravity-agents-repository/scripts/pipeline_sprint1_parcelas_manzanas_alta_resolucion.py).
- **Particionamiento**: Jerárquico por Circunscripción y Sección (`nomenclatura LIKE '11-01-01-CC-SS%'`), evitando timeouts del servidor WFS (`maaysp-ws.cba.gov.ar`).
- **Persistencia**: Caché en disco en `data/cache_parcelas_wfs/circ_CC_sec_SS.json` con tolerancia a cortes de conexión y reanudación automática.

### B. Consolidación y Recomposición Topológica de Manzanas
- **Universo Procesado en Circunscripción 01 (Centro Histórico / Nueva Córdoba / Macrocentro)**:
  - **53.039 registros WFS** descargados e indexados.
  - **34.891 parcelas oficiales únicas** consolidadas con asignación de calles perimetrales.
  - **1.617 Manzanas Sintéticas de Alta Resolución** generadas por disolución exacta en solo **1.23 segundos**.
  - **Superficie**: Mediana de **0.61 ha** por manzana (tamaño urbanístico real de Córdoba).
  - **Densidad**: Mediana de **23 parcelas** por manzana.
  - **Trama Vial**: 100% preservada abierta (calles, pasajes y avenidas limpios y sin deformaciones).

### C. Entregables Generados y Espejados
1. **GeoJSON**: `data/manzanas_alta_resolucion_distrito1.geojson` (2.66 MB).
2. **GeoParquet**: `data/manzanas_alta_resolucion_distrito1.parquet` (0.83 MB).
3. **Módulo Autónomo**: `data/manzanas_alta_resolucion_data.js` (2.66 MB), espejado en:
   - `D:\Usuarios\jidiaz\Downloads\data\manzanas_alta_resolucion_data.js`
   - `C:\Usuarios\jidiaz\Downloads\data\manzanas_alta_resolucion_data.js`
4. **Visor Interactivo Leaflet & ESRI**:
   - `D:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_piloto.html`
   - `C:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_piloto.html`

---

## 3. Triple QA Gate

| Instancia | Criterio Evaluado | Resultado |
| :--- | :--- | :--- |
| **QA 1: Algorítmico & Técnico** | `shapely.ops.unary_union` sobre EPSG:22174 métrico, cero errores de topología inválida y reproyección a WGS84. | ✅ APROBADO (17.01s total) |
| **QA 2: Dominio & Negocio** | Identificación de manzana mediante 6 tokens (`11-01-01-CC-SS-MMM`), preservando 520 a 1.617 manzanas urbanas reales. | ✅ APROBADO |
| **QA 3: Usabilidad & UX** | Visor HTML autónomo ejecutable por doble clic con ESRI World Street Map e inspección de calles en hover. | ✅ APROBADO |
