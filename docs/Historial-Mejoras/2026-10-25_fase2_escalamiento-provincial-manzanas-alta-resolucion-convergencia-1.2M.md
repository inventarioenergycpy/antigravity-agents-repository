---
title: "Registro de Mejora: Escalamiento Provincial Unificado de Manzanas de Alta Resolución y Motor de Convergencia en 1.2M Suministros (Fase 2)"
tags:
  - #historial-mejoras
  - #fase-2
  - #escalamiento-provincial
  - #gis
  - #catastro
  - #epec-parcelas-union
  - #convergencia-suministros
  - #arquetipo-a
date: 2026-10-25
author: Squad Arquetipo A & Project Manager (Gemini 3.8 Flash High)
---

# 🚀 Registro de Mejora: Escalamiento Provincial Unificado de Manzanas de Alta Resolución y Motor de Convergencia en 1.2M Suministros (Fase 2)

- **Fecha**: 25 de Octubre de 2026
- **Hito**: Fase 2 — Escalamiento Provincial Unificado (Arquetipo A: GIS, Catastro & Rutas EPEC)
- **Squad Ágil**: PM (*Gemini 3.8 Flash High*) & 3 Operadores (*Gemini 3.7 Flash High*)
- **Estado**: ✅ CONSOLIDADO, VALIDADO Y DESPLEGADO

---

## 1. Contexto y Desafío de Escalamiento a Nivel Provincial

Tras el éxito del piloto en Circunscripción 01 (Sprints 1, 2 y 3), se ejecutó la extensión total sobre el universo cartográfico oficial de **`EPEC:vm_vt_parcelas_calles`** y la base comercial completa de **`georef.vw_suministros`**.

El desafío técnico radicó en procesar de forma masiva e incremental:
1. **953.367 registros parcelarios** distribuidos en 571 chunks espaciales sobre GeoServer WFS sin generar sobrecarga ni timeouts.
2. **1.208.097 suministros comerciales** de los 48 distritos de EPEC extraídos en streaming por lotes de 50.000 desde Oracle.
3. **Disolución topológica vectorizada (`unary_union`)** en POSGAR 94 (`EPSG:22174`) para sintetizar **33.655 Manzanas de Alta Resolución**.
4. **Motor de Convergencia Multivariada en 4 Partes** y **Propagación por Vecindad de Ruta ($\pm 3$)** sobre más de 5.000 rutas operativas.

---

## 2. Resultados Cuantitativos Consolidados (Provincia de Córdoba)

### Balance Global de Suministros (1.208.097 Evaluados)

| Nivel de Certeza | Cantidad de Suministros | Porcentaje | Descripción y Tratamiento Operativo |
| :--- | :--- | :--- | :--- |
| 🟢 **Nivel 1A (DC Catastral Exacta)** | **700.116** | **57.95%** | Asignación parcelaria directa e irreversible. |
| 🟢 **Nivel 1B (Multi-criterio $\ge 3$ partes)** | **53.049** | **4.39%** | Alta certeza confirmada por consenso de 3 o 4 dimensiones. |
| 🟢 **Nivel 1C (Alta Revalidada por Vecinos)** | **18.263** | **1.51%** | Promovidos por consenso unánime de ruta contigua ($\pm 3$). |
| 🏆 **TOTAL ALTA CERTEZA (Nivel 1)** | **771.428** | **63.85%** | **Núcleo consolidado de asignación parcelaria oficial.** |
| 🟡 **Nivel 2 (Certeza Media / Ambiguo)** | **10.362** | **0.86%** | Coincidencia en 2 dimensiones; casos puntuales para auditoría. |
| 🟠 **Nivel 3 (Asignación Parcial a Manzana)** | **3.791** | **0.31%** | Parcela individual dudosa, pero pertenencia a Manzana confirmada. |
| 🔴 **Nivel 4 (Sin Coincidencia / Discrepancia)** | **422.516** | **34.97%** | Localidades del interior y zonas rurales sin cobertura parcelaria en WFS. |
| 🌐 **COBERTURA TERRITORIAL ÚTIL (N1 + N3)** | **775.219** | **64.17%** | **Suministros integrados a manzanas y parcelas de alta resolución.** |

### Foco Estratégico: Distrito 1 (Capital - 619.707 Suministros)

En la Ciudad de Córdoba, donde la cobertura de la capa parcelaria `EPEC:vm_vt_parcelas_calles` es exhaustiva (625.840 registros en 35 Circunscripciones):
- **Alta Certeza (Nivel 1)**: **567.637 suministros (91.60%)**.
- **Cobertura Territorial Útil (N1 + N3)**: **569.369 suministros (91.88%)**.
- En el interior provincial con cobertura cartográfica (Distrito 8 Río Cuarto / Punilla), la certeza alcanzó el **74.85%**.

---

## 3. Arquitectura de Recomposición y Catálogo Jerárquico

Se estructuraron **55 particiones territoriales autónomas**:
- **Capital (Departamento 11)**: 35 Circunscripciones (`11_C01` a `11_C35`) con **26.471 manzanas sintéticas** y **580.330 parcelas únicas**.
- **Interior Provincial**: 20 Pedanías en 8 Departamentos (Colón, Río Cuarto, Cruz del Eje, Santa María, Tercero Arriba, Punilla, San Justo, Río Primero) con **7.184 manzanas sintéticas**.

Cada manzana sintética cuenta con:
- Límite perimetral geométrico continuo sin huecos ni solapes.
- Lista consolidada de nombres de calles frentistas y rango de numeración municipal.
- Conteo de parcelas constitutivas, área neta en hectáreas y perímetro en metros.

---

## 4. Despliegue del Visor Web Jerárquico Standalone (60 FPS)

Para evitar la saturación del DOM al cargar polígonos masivos, se implementó una **arquitectura de carga bajo demanda (Lazy Loading)**:
- El navegador carga inicialmente solo el **Catálogo Jerárquico** (`catalogo_jerarquico_data.js`, 50 KB).
- El usuario selecciona **Departamento** $	o$ **Circunscripción / Pedanía**.
- Se inyecta dinámicamente el fragmento vectorial correspondiente (`mzas_11_C01.js`, etc.), manteniendo la memoria activa por debajo de 30 MB y garantizando una tasa de refresco constante de **60 FPS**.
- Totalmente compatible con ejecución offline directa (`file:///`).

---

## 5. Entregables Generados

1. **Visor Web Interactivo Provincial**:
   - `D:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_provincial.html`
   - `C:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_provincial.html`
   - `visor_manzanas_hr_provincial.html`
2. **Datasets Consolidados Parquet**:
   - `data/suministros_provincial_completo.parquet` *(58.63 MB, 1.208.097 suministros)*
   - `data/manzanas_alta_resolucion_provincial.parquet` *(33.655 manzanas sintéticas)*
   - `data/convergencia_suministros_provincial_final.parquet` *(66.70 MB, resultados consolidados)*
3. **Catálogo y Particiones Vectoriales**:
   - `data/catalogo_jerarquico_provincial.json` & `data/catalogo_jerarquico_data.js`
   - 55 archivos GeoJSON y JS en `data/manzanas_por_circ/`
4. **Scripts del Pipeline**:
   - `scripts/pipeline_descarga_masiva_wfs_chunks.py`
   - `scripts/extraer_suministros_provincial.py`
   - `scripts/pipeline_sintesis_manzanas_provincial.py`
   - `scripts/ejecutar_convergencia_provincial.py`
