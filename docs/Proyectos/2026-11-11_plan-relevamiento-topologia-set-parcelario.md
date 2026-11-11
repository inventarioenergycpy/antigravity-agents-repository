---
title: "Plan de Relevamiento, Topología de Subestaciones & Fusión Parcelaria EPEC"
tags:
  - #proyecto
  - #protelem-epec
  - #gis
  - #catastro
  - #subestaciones
  - #tarifa-social
  - #arquetipo-a
  - #squad-multi-agente
created: 2026-11-11
actualizado: 2026-11-11
estado: FASE 6 FINALIZADA (100% Validado con Triple QA)
autor: Squad Ágil PM-Operadores (Arquetipo A) & Copiloto Orquestador
repositorio_dedicado: "https://github.com/PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario.git"
workspace_local: "file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario"
---

# ⚡ Plan de Relevamiento, Topología de Subestaciones & Fusión Parcelaria EPEC

## 1. Resumen Ejecutivo y Ficha Técnica
Proyecto geoespacial y de ingeniería comercial desarrollado bajo la gobernanza del **Squad Ágil Multi-Agente PM-Operadores (Arquetipo A: GIS, Catastro y Redes Eléctricas)** para consolidar el parcelario provincial de EPEC, auditar las fronteras de 5.296 Subestaciones Transformadoras (SET), clasificar la red según volumen de demanda e identificar el universo de usuarios con Tarifa Social Oficial (Decreto Provincial 43/2019).

- **Repositorio Dedicado GitHub**: [PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario](https://github.com/PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario.git)
- **Directorio Local**: [`D:\Proyectos\plan-relevamiento-topologia-set-parcelario`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario)
- **Visor Interactivo**: [`viewer/index.html`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/viewer/index.html)

---

## 2. Arquitectura de Fusión Jerárquica Parcelaria
Para evitar duplicidades y superposiciones, se aplicó una matriz de prioridad estricta para la consolidación de capas:
1. **Prioridad 1 (Máxima)**: `EPEC:parcelas_union` (`vt_parcelas_union` / `vm_vt_parcelas_union`).
2. **Prioridad 2 (Media)**: Municipalidad de Córdoba (`parcelas_muni` / `parcelas_muni_4326`).
3. **Prioridad 3 (Base)**: Provincia de Córdoba - IDECOR (`parcelas_idecor`).

**Regla Topológica y Catastral**: Saneamiento estricto de números de parcela duplicados en una misma manzana (69.011 anomalías aisladas en log), consolidando una **Capa Maestra Saneada de 386.005 parcelas únicas** en [`data/capa_parcelas_general_consolidada.parquet`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/data/capa_parcelas_general_consolidada.parquet).

---

## 3. Auditoría Topológica de Subestaciones (SET) y Log de Excepciones

- **Universo de Subestaciones Analizado**: 5.296 polígonos de `EPEC:vt_subestaciones_poly` en EPSG:4326.
- **Cobertura Neta**: 311.912 parcelas (80.9%) ubicadas dentro de los polígonos de SET.
- **Parcelas Cortadas por el Perímetro de SET**:
  - En cumplimiento de la decisión acordada en la Compuerta de Clarificación (Respuesta A3), se mantuvo la **frontera rígida** de las subestaciones y se catalogaron **110.230 parcelas cortadas** en [`reports/log_excepciones_parcelas_cortadas_frontera.csv`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/reports/log_excepciones_parcelas_cortadas_frontera.csv) para control y verificación manual por cuadrilla.

---

## 4. Diagnóstico de Tarifa Social y Sensibilidad (Decreto 43/2019)

Sobre el padrón provincial de 1.208.097 suministros se identificaron **94.256 usuarios bajo Tarifa Social Oficial**:
- `Resid TSP Caren Dto. 43/19`: 46.941 suministros.
- `Resid TSP Indig Dto. 43/19`: 38.244 suministros.
- `Social Prov. sin medición`: 9.065 suministros.
- `1.a/f RES.SOCIAL PROV. INDIG.`: 6 suministros.

**Subestaciones Críticas**: Se identificaron **621 SETs con Alta Sensibilidad Social ($\ge 20\%$ de Tarifa Social)**, etiquetadas con `TARIFA_SOCIAL = TRUE` para la aplicación del protocolo de sensibilidad comercial acordado (Respuesta A2).

---

## 5. Clasificación de Subestaciones

| Categoría | Rango de Suministros | Subestaciones | % del Total |
| :--- | :---: | :---: | :---: |
| **MEGA_SET** | $\ge 1.000$ sumis | `1` | 0.02% |
| **GRANDE** | $500 - 999$ sumis | `31` | 0.59% |
| **MEDIANA** | $150 - 499$ sumis | `1,226` | 23.15% |
| **PEQUEÑA** | $1 - 149$ sumis | `3,164` | 59.74% |
| **SIN_SUMINISTROS** | $0$ sumis | `874` | 16.50% |
| **TOTAL** | - | **5,296** | **100.0%** |
