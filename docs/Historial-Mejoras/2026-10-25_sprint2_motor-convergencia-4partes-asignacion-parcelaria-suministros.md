---
title: "Registro de Mejora: Motor de Convergencia en 4 Partes para Asignación Parcelaria de Suministros (Sprint 2)"
tags:
  - #historial-mejoras
  - #sprint-2
  - #gis
  - #catastro
  - #convergencia-suministros
  - #oracle-georef
  - #arquetipo-a
date: 2026-10-25
author: Squad Arquetipo A & Project Manager (Gemini 3.8 Flash High)
---

# 📜 Registro de Mejora: Motor de Convergencia en 4 Partes para Asignación Parcelaria de Suministros (Sprint 2)

- **Fecha**: 25 de Octubre de 2026
- **Sprint**: Sprint 2 — Arquetipo A (GIS, Catastro & Rutas EPEC)
- **Squad Ágil**: PM (*Gemini 3.8 Flash High*) & 3 Operadores (*Gemini 3.7 Flash High*)
- **Estado**: ✅ CONSOLIDADO, VALIDADO Y DESPLEGADO

---

## 1. Contexto y Desafío de Convergencia

Para vincular con máxima certeza los **585.727 suministros de EPEC Distrito 1** con el catastro parcelario oficial sin forzar asignaciones erróneas, se diseñó e implementó un **Motor de Convergencia Multivariada en 4 Partes**, evaluando simultáneamente:

1. **Dimensión 1 (DC Exacta)**: Hash alfanumérico normalizado de 16/18 dígitos (`DC` de `vw_suministros` vs `nomenclatura` de parcela o manzana).
2. **Dimensión 2 (Cuaterna Catastral SIGEC)**: Recomposición paramétrica de `(DISTRITO, ZONA, MANZANA, LOTE)` frente a las claves cartográficas oficiales.
3. **Dimensión 3 (Dirección Postal Toponímica)**: Normalización toponímica de `CALLE` + `ALTURA` frente a las calles perimetrales de la manzana y frentes de parcela (`EPEC:vm_vt_parcelas_calles`).
4. **Dimensión 4 (Geolocalización Espacial)**: Point-in-Polygon espacial mediante índice acelerado `STRtree` de Shapely contra las 1.617 Manzanas Sintéticas de Alta Resolución.

---

## 2. Resultados Cuantitativos del Sprint 2 (Circunscripción 01)

Sobre el universo completo de **66.529 suministros comerciales** de Circunscripción 01 (Centro, Nueva Córdoba, Güemes, Alberdi, etc.), se obtuvieron los siguientes resultados tras una ejecución analítica de **5.65 segundos** (11.782 sum/s):

| Categoría de Convergencia | Cantidad de Suministros | Porcentaje | Tratamiento y Destino Operativo |
| :--- | :--- | :--- | :--- |
| 🟢 **Nivel 1A (Coincidencia DC Exacta)** | **49.787** | **74.84%** | Asignación parcelaria directa e irreversible. |
| 🟢 **Nivel 1B (Multi-criterio $\ge 3$ dimensiones)** | **5.653** | **8.50%** | Alta certeza confirmada por consenso de 3 o 4 dimensiones. |
| **TOTAL ALTA CERTEZA (Nivel 1)** | **55.440** | **83.33%** | **Suministros ancla consolidados para el ruteo.** |
| 🟡 **Nivel 2 (Certeza Media / Requiere Vecinos)** | **3.113** | **4.68%** | Coinciden 2 dimensiones. Se derivan a convalidación en Sprint 3 por vecindad de ruta (`orden_lectura ± 3`). |
| 🟠 **Nivel 3 (Asignación Parcial a Manzana)** | **5.567** | **8.37%** | Parcela individual con ambigüedad de lote, pero pertenencia a Manzana Sintética confirmada. Asignación a nivel manzana con flag de alerta. |
| 🔴 **Nivel 4 (Sin Coincidencia / Discrepancia Total)** | **2.409** | **3.62%** | Casos atípicos para auditoría manual o revisión de datos comerciales. |
| **UNIVERSO TOTAL EVALUADO** | **66.529** | **100.00%** | **Circunscripción 01 completo.** |

---

## 3. Modelo Relacional 1 a N para Propiedad Horizontal (PH)

- **Validación Exitosa**: Se identificaron **24.785 parcelas físicas únicas** con al menos 1 suministro anclado.
- **Micro-clustering de PHs**:
  - Parcela `11-01-01-01-24-025-011`: **584 suministros** vinculados a la misma geometría base.
  - Parcela `11-01-01-01-01-009-009`: **337 suministros**.
  - Parcela `11-01-01-01-24-028-022`: **223 suministros**.
- Se preserva la geometría única sin duplicar polígonos, manteniendo la base cartográfica ligera y responsiva.

---

## 4. Entregables Generados

1. **Dataset de Clasificación Parquet**:
   - `data/convergencia_suministros_circ01.parquet` (0.85 MB — 66.529 registros clasificados por nivel de certeza y flags).
2. **Caché de Suministros Originales**:
   - `data/suministros_circ01.parquet` (1.42 MB — volcado local de Oracle).
3. **Visor Cartográfico Interactivo Actualizado**:
   - `D:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_piloto.html`
   - `C:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_piloto.html`
   - Incorpora el balance del Sprint 2 y tarjetas dinámicas con conteo de suministros y % de alta certeza por manzana.
4. **Script Rector**:
   - [`scripts/ejecutar_sprint2_convergencia_4partes.py`](file:///D:/Proyectos/antigravity-agents-repository/scripts/ejecutar_sprint2_convergencia_4partes.py).

---

## 5. Triple QA Gate

| Instancia | Criterio Evaluado | Resultado |
| :--- | :--- | :--- |
| **QA 1: Algorítmico & Rendimiento** | Normalización toponímica regex, evaluación espacial STRtree en 5.65s (11.782 reg/s), sin fugas de memoria. | ✅ APROBADO |
| **QA 2: Dominio & Negocio** | Respeto irrestricto de las reglas fijadas por el usuario: 1-DC manda para Alta Certeza; 3-4 partes es Alta; 2 partes deriva a vecinos; fallback a manzana notificado. | ✅ APROBADO |
| **QA 3: Usabilidad & Replicabilidad** | Visor HTML actualizado con leyenda de densidad, métricas de balance y ejecución offline doble clic. | ✅ APROBADO |
