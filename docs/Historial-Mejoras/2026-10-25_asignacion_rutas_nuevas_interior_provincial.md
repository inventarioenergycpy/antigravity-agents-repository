---
title: "Registro de Mejora: Extensión de Asignación de Rutas Nuevas al Interior Provincial y Consolidación Maestro"
tags:
  - #historial-mejoras
  - #rutas-nuevas
  - #interior-provincial
  - #convergencia-parcelaria
  - #sigec
  - #grafo-calles
  - #rio-cuarto
  - #villa-maria
  - #carlos-paz
  - #arquetipo-a
date: 2026-10-25
author: Squad Arquetipo A & Project Manager (Gemini 3.8 Flash High)
sprint: 5
status: APROBADO_CONSOLIDADO
---

# 🚀 Registro de Mejora: Extensión de Asignación de Rutas Nuevas al Interior Provincial y Consolidación Maestro

- **Fecha**: 25 de Octubre de 2026
- **Área**: Dirección de Tecnología y Sistemas Comerciales / Medición y Facturación EPEC
- **Squad Ágil**: PM (*Gemini 3.8 Flash High*) & Operadores (*Gemini 3.7 Flash High*)
- **Estado**: ✅ CONSOLIDADO, AUDITADO Y DESPLEGADO

---

## 1. Contexto y Objetivos

Habiendo validado y consolidado el motor de asignación de rutas nuevas sobre Distrito 1 (Capital), el usuario solicitó extender el mismo motor de asignación al bloque de **distritos del interior provincial con cobertura parcelaria**.

El bloque incluye **9 distritos comerciales neurálgicos** de la provincia de Córdoba:
- **Distrito 28**: Río Cuarto (89.061 suministros)
- **Distrito 8**: Villa María (63.282 suministros)
- **Distrito 47**: Villa Carlos Paz (56.930 suministros)
- **Distrito 45**: Alta Gracia (38.081 suministros)
- **Distrito 18**: San Francisco (36.781 suministros)
- **Distrito 22**: Río Ceballos (30.734 suministros)
- **Distrito 23**: Villa Allende (29.368 suministros)
- **Distrito 24**: La Calera (16.168 suministros)
- **Distrito 21**: Santiago Temple (1.527 suministros)

---

## 2. Resultados Consolidados por Distrito del Interior

El motor procesó los **361.932 suministros** del interior cubierto en **3,49 minutos**, logrando un cumplimiento de **88,3% en la banda contractual óptima [160, 200]**:

| Distrito | Nombre / Cabecera | Suministros | Rutas Anteriores | Rutas Nuevas | Promedio Anterior | Promedio Nuevo | Mediana Nueva | Rutas en Tol. [160-200] | % Cumplimiento |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **D28** | Río Cuarto | 89.061 | 423 | **534** | 210,5 | 166,8 | 172 | 478 | **91,7%** |
| **D08** | Villa María | 63.282 | 283 | **382** | 223,6 | 165,7 | 171 | 340 | **91,9%** |
| **D47** | Villa Carlos Paz | 56.930 | 154 | **355** | 369,7 | 160,4 | 169 | 314 | **91,0%** |
| **D45** | Alta Gracia | 38.081 | 154 | **261** | 247,3 | 145,9 | 159 | 210 | **84,0%** |
| **D18** | San Francisco | 36.781 | 221 | **223** | 166,4 | 164,9 | 170 | 202 | **94,0%** |
| **D22** | Río Ceballos | 30.734 | 134 | **209** | 229,4 | 147,1 | 157 | 175 | **86,2%** |
| **D23** | Villa Allende | 29.368 | 155 | **186** | 189,5 | 157,9 | 167 | 162 | **90,5%** |
| **D24** | La Calera | 16.168 | 63 | **105** | 256,6 | 154,0 | 164 | 78 | **78,8%** |
| **D21** | Santiago Temple | 1.527 | 15 | **20** | 101,8 | 76,4 | 75 | 8 | **44,4%** |
| **TOTAL** | **INTERIOR CUBIERTO** | **361.932** | **1.602** | **2.275** | **225,9** | **159,3** | **168,0** | **1.967** | **88,3%** |

---

## 3. Padrón Consolidado Provincial (Distrito 1 + Interior)

| Nivel Territorial | Suministros Totales | Rutas Nuevas Creadas | Promedio Sum/Ruta | Mediana Sum/Ruta | % En Rango [160, 200] |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Distrito 1 (Capital)** | 619.707 | 3.793 | 163,4 | 169,0 | 77,5% |
| **Interior Cubierto (9 Distritos)** | 361.932 | 2.272 | 159,3 | 168,0 | 88,3% |
| **TOTAL PROVINCIAL CONSOLIDADO** | **981.639** | **6.065** | **161,8** | **168,0** | **81,6%** |

---

## 4. Entregables Generados

1. **Padrón Maestro Provincial Consolidado**:
   - `data/summary/padron_nuevas_rutas_provincial_consolidado.parquet` (36,58 MB, 981.639 registros).
   - `D:\Usuarios\jidiaz\Downloads\padron_nuevas_rutas_provincial_consolidado.csv` (270,92 MB).
   - `C:\Users\jidiaz\Downloads\padron_nuevas_rutas_provincial_consolidado.csv` (270,92 MB).
2. **Capa Geoespacial de Rutas Vectoriales Provincial**:
   - `data/summary/rutas_nuevas_poligonos_provincial.geojson` (129,48 MB, 6.065 polígonos vectoriales).
   - `data/summary/rutas_nuevas_poligonos_provincial.parquet` (38,96 MB).
   - `D:\Usuarios\jidiaz\Downloads\rutas_nuevas_poligonos_provincial.geojson` (129,48 MB).
3. **Resúmenes Ejecutivos**:
   - `data/summary/resumen_todas_rutas_nuevas_provincial.csv` (767 KB, 6.065 rutas).
   - `data/summary/resumen_comparativo_interior.csv` (3,4 KB).
4. **Scripts Versionados**:
   - `scripts/ejecutar_asignacion_rutas_nuevas_interior.py`.
