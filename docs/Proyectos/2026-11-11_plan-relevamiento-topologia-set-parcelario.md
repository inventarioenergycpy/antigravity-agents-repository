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
actualizado: 2026-11-12
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
- **Reporte por Plan de Relevamiento**: [`reports/resumen_plan_relevamiento_clientes_cc_vs_otros.csv`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/reports/resumen_plan_relevamiento_clientes_cc_vs_otros.csv)

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

---

## 6. Resumen por Plan de Relevamiento: Clientes Comunes (CC) vs. Otros Tipos de Clientes

En los **20 Planes Principales de Relevamiento de Córdoba Capital (Distrito 1)** se censaron **585.819 puntos de suministro**:
- **Clientes Comunes (CC)**: **537.633 suministros (91.77%)** (Tarifas 1 Residencial y 2 Comercial/General BT).
- **Otros Tipos de Clientes**: **48.186 suministros (8.23%)**, de los cuales **45.799 son Tarifa Social** (95.0% de los no comunes).

### Matriz Sintética por Plan (Planes 01 al 20)

| Plan | Puntos Totales | Clientes Comunes (CC) | % CC | Otros Clientes | % Otros | Tarifa Social | Oficial / Gob. | AP / Otros | Perfil Operativo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Plan 01** | 29.910 | 29.470 | **98.53%** | 440 | 1.47% | 348 | 59 | 33 | Residencial Masivo Alto CC |
| **Plan 02** | 19.856 | 19.070 | **96.04%** | 786 | 3.96% | 721 | 44 | 21 | Residencial / Comercial Urbano |
| **Plan 03** | 38.204 | 33.737 | **88.31%** | 4.467 | 11.69% | 4.306 | 96 | 65 | Mixto con Foco Tarifa Social |
| **Plan 04** | 24.285 | 24.047 | **99.02%** | 238 | 0.98% | 155 | 65 | 18 | Residencial Homogéneo CC |
| **Plan 05** | 27.593 | 22.767 | **82.51%** | 4.826 | **17.49%** | 4.695 | 80 | 51 | Alta Sensibilidad Social |
| **Plan 06** | 12.675 | 11.617 | **91.65%** | 1.058 | 8.35% | 1.002 | 39 | 17 | Mixto Noreste (Lote 1) |
| **Plan 07** | 25.216 | 21.700 | **86.06%** | 3.516 | **13.94%** | 3.397 | 65 | 54 | Foco Tarifa Social Suburbana |
| **Plan 08** | 27.622 | 27.117 | **98.17%** | 505 | 1.83% | 405 | 85 | 15 | Este Masivo Residencial CC |
| **Plan 09** | 16.863 | 14.162 | **83.98%** | 2.701 | **16.02%** | 2.598 | 60 | 43 | Mixto con Reclamos Vulnerables |
| **Plan 10** | 17.360 | 13.763 | **79.28%** | 3.597 | **20.72%** | 3.502 | 55 | 40 | **Crítico: >20% Tarifa Social** |
| **Plan 11** | 24.233 | 18.662 | **77.01%** | 5.571 | **22.99%** | 5.413 | 81 | 77 | **Crítico: 23% Tarifa Social** |
| **Plan 12** | 22.098 | 21.206 | **95.96%** | 892 | 4.04% | 812 | 61 | 19 | Sureste Residencial CC |
| **Plan 13** | 34.498 | 31.844 | **92.31%** | 2.654 | 7.69% | 2.520 | 74 | 60 | Mixto Comercial / Residencial |
| **Plan 14** | 47.912 | 47.772 | **99.71%** | 140 | 0.29% | 26 | 99 | 15 | **Centro-Nueva Cba: 100% CC** |
| **Plan 15** | 30.593 | 30.311 | **99.08%** | 282 | 0.92% | 71 | 163 | 48 | Centro-Norte Residencial CC |
| **Plan 16** | 47.984 | 41.914 | **87.35%** | 6.070 | 12.65% | 5.893 | 108 | 69 | Volumen Masivo con Asentamientos |
| **Plan 17** | 34.787 | 34.065 | **97.92%** | 722 | 2.08% | 588 | 117 | 17 | Centro-Sur Aéreo / Subterráneo CC |
| **Plan 18** | 33.248 | 27.497 | **82.70%** | 5.751 | **17.30%** | 5.605 | 79 | 67 | Oeste Mixto / Arranque |
| **Plan 19** | 29.408 | 28.313 | **96.28%** | 1.095 | 3.72% | 998 | 72 | 25 | Residencial Nansen Homogéneo |
| **Plan 20** | 41.474 | 38.599 | **93.07%** | 2.875 | 6.93% | 2.744 | 76 | 55 | Mixto de Gran Extensión Periférica |
| **TOTAL** | **585.819** | **537.633** | **91.77%** | **48.186** | **8.23%** | **45.799** | **1.578** | **809** | **20 Planes Principales** |

### Planes Especiales de Relevamiento de Ingeniería
- **`TLMD` (Telemedidos)**: 1.597 puntos (1.112 Grandes Clientes / Tarifa 3, 95.5% otros clientes).
- **`ZALT` (Alumbrado Público)**: 1.835 puntos (1.790 Alumbrado Vialidad, 99.7% otros clientes).
- **`ZSLEC` (Sin Lectura / Organismos)**: 4.936 puntos (3.443 dependencias públicas/oficiales, 72.5% otros clientes).
- **`Plan 99` (Asentamientos)**: 17.992 puntos (8.896 Tarifa Social, 51.1% otros clientes).

---

## 7. Plan de Relevamiento a Futuro & Auditoría de Calidad de Polígonos

A partir del cruce de `georef.relevamiento` (473.762 suministros registrados en campo) con los polígonos de las 5.296 Subestaciones Transformadoras (SET) y el padrón de rutas de lectura, se obtuvieron las directrices estratégicas de despliegue:

### 1. Balance de Relevamiento Distrito 1 (Córdoba Capital - 20 Planes)
- **Puntos Totales**: **585.819 suministros**
- **Relevamiento Histórico Efectivo**: **348.673 suministros (59,52% de avance)**
- **Backlog Futuro a Relevar**: **237.146 suministros (40,48% pendiente)**
  - *Pendientes Clientes Comunes (CC)*: **220.395 suministros (92,94%)**
  - *Pendientes Tarifa Social (TSP)*: **15.947 suministros (6,72%)**
  - *Pendientes Otros*: **804 suministros (0,34%)**

### 2. Calidad Topológica de los Polígonos de Subestaciones
- **ALTA_LIMPIO (0 parcelas cortadas)**: `963` SETs (18,18%) $\rightarrow$ 5.776 sumis pendientes. Límites viales limpios.
- **ALTA_LEVE (1 a 10 parcelas cortadas)**: `1.278` SETs (24,13%) $\rightarrow$ 18.944 sumis pendientes. Conflicto perimetral mínimo.
- **MEDIA_MODERADO (11 a 30 parcelas cortadas)**: `973` SETs (18,37%) $\rightarrow$ 31.294 sumis pendientes. Requiere plano de detalle en bordes.
- **BAJA_CONFLICTO (> 30 parcelas cortadas)**: `1.923` SETs (36,31%) $\rightarrow$ 82.453 sumis pendientes. Frontera divide parcelas y manzanas al medio.

### 3. Matriz de Priorización Operativa en 5 Cuadrantes
| Cuadrante | SETs | Suministros Pendientes | Tarifa Social | Directriz de Despliegue |
| :--- | :---: | :---: | :---: | :--- |
| **`1_RELEVAMIENTO_INMEDIATO`** | **387** | **44.699** | 2.264 | **Despacho Inmediato**: Polígonos limpios, alta demanda CC pendiente. Máxima productividad. |
| **`2_SENSIBILIDAD_SOCIAL`** | **105** | **7.194** | 2.546 | **Atención Comunitaria**: $\ge 20\%$ Tarifa Social. Protocolo con centros vecinales y mediadores. |
| **`3_SANEAMIENTO_TOPOLOGICO_PREVIO`** | **449** | **78.898** | 5.822 | **BLOQUEADO EN CAMPO**: Polígonos con severo conflicto perimetral. **Ajustar límites en GIS antes de salir a campo**. |
| **`4_AVANZADA_O_COMPLETADA`** | **3.481** | **7.676** | 26.585 | **Barrido Final**: Avance $\ge 75\%$ o remanente $< 30$ sumis (423.101 ya relevados). |
| **`5_SIN_DEMANDA_O_ESPECIAL`** | **715** | **0** | 0 | **Especiales**: SETs industriales o sin demanda directa. |

### 4. Focos Críticos de Relevamiento por Plan
- **Prioridad 1 Masiva CC (0% a 2% avance histórico)**:
  - **Plan 14 (Centro / Nueva Cba)**: 47.879 pendientes (47.764 CC $\rightarrow$ 99,8% CC).
  - **Plan 15 (Centro Norte)**: 29.995 pendientes (29.751 CC $\rightarrow$ 99,2% CC).
  - **Plan 08 (Este Residencial)**: 27.535 pendientes (27.061 CC $\rightarrow$ 98,3% CC).
  - **Plan 17 (Centro-Sur)**: 19.496 pendientes (19.391 CC $\rightarrow$ 99,5% CC).
- **Prioridad Sensibilidad Social**:
  - **Plan 11**: 23.793 pendientes (5.335 Tarifa Social $\rightarrow$ 22,4% vulnerable).
  - **Plan 07**: 24.348 pendientes (3.285 Tarifa Social).
  - **Plan 09**: 16.047 pendientes (2.507 Tarifa Social).
- **Planes en Fase Final de Barrido (> 80% avance)**:
  - Planes 01, 02, 03, 04, 05, 06, 10, 13, 16, 18, 19 y 20 (33.376 puntos remanentes combinados).

### 5. Estimación de Plazos a Régimen de 10.000 Relevamientos/Mes
Para un despliegue operativo sostenido de **10.000 relevamientos/mes** (~476 suministros/día hábil con 16 a 20 cuadrillas en paralelo):

* **Planes Vírgenes Sin Relevamiento (< 5% avance: Planes 14, 15, 08, 07, 11 y 09)**:
  * Universo: **169.597 suministros**.
  * Plazo Estimado: **16,96 meses (~17 meses corridos $\approx$ 1 año y 5 meses)**.
  * Fecha estimada de finalización: **Fines de Abril / Mayo 2028**.
* **Planes Incompletos (< 80% avance: 9 planes)**:
  * Universo: **204.048 suministros**.
  * Plazo Estimado: **20,40 meses (~1 año y 8,5 meses)**.
* **Universo Total Consolidado (20 Planes al 100%)**:
  * Universo: **237.146 suministros**.
  * Plazo Estimado: **23,71 meses (~2 años exactos)**.

### 6. Caracterización Parcelaria por Plan (Fronteras SET y Parcelas a Dibujar)
A partir del cruce tridimensional entre los 20 Planes, la capa de parcelas consolidadas y el log de excepciones de frontera:
- **Total Parcelas Dibujadas**: `266.755` parcelas territoriales activas con suministros en los 20 planes.
- **Parcelas en Frontera de SET (a analizar por cuadrilla)**: `88.205` parcelas (33,07% del parcelario).
  - Máxima concentración: Plan 16 (10.039), Plan 18 (7.620), Plan 03 (7.343), Plan 20 (6.784).
  - Mínimo conflicto: Plan 14 (21 parcelas, 0,99%) y Plan 15 (106 parcelas, 3,62%) debido a red subterránea y topología compacta.
- **Parcelas a Dibujar (Faltantes en Cartografía)**: `26.736` parcelas identificadas a partir de la descripción catastral normalizada (`dc` / `id_suministro_catastral`) de suministros activos que carecen de polígono vectorial.
  - Foco de digitalización: Plan 05 (3.017), Plan 09 (2.872), Plan 16 (2.834), Plan 11 (2.719), Plan 07 (2.555).
- Reporte detallado disponible en: [`docs/07_analisis_parcelas_fronteras_y_faltantes_a_dibujar_por_plan.md`](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/docs/07_analisis_parcelas_fronteras_y_faltantes_a_dibujar_por_plan.md).

