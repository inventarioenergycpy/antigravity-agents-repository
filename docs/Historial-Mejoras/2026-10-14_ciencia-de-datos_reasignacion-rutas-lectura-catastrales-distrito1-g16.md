---
type: historial_mejora
agente: "[[docs/Agentes/02-Ciencia-de-Datos|02 - Ciencia de Datos & Ingeniero de Analytics BI]]"
fecha: 2026-10-14
proyecto: "[[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas|Control de Rutas de Lecturas - Nuevas Rutas]]"
tags:
  - #catastro
  - #ruteo-lectura
  - #epec
  - #distrito1
  - #grupo16
  - #bin-packing
  - #wfs
---

# 🚀 Historial de Mejora: Reorganización Catastral de Rutas de Lectura - Piloto Distrito 1 / Grupo 16

## 📌 Contexto y Diagnóstico
En la base de datos comercial y técnica de EPEC (`georef.vw_suministros`), los suministros se organizan tradicionalmente en `distrito`, `grupo_lectura`, `ruta_lectura` y `orden_lectura`. Las rutas actuales presentan una alta dispersión (entre 10 y más de 1.000 suministros por ruta), saltos geográficos entre manzanas no colindantes y desconexión con la cartografía catastral provincial oficial de Catastro y Rentas de Córdoba.

## 🎯 Solución Diseñada e Implementada
1. **Nuevo Identificador Catastral de Suministro**:
   - Estructura: `DISTRITO-GRUPO_LECTURA-NOMENCLATURA_MANZANA_WFS-PARCELA`
   - Ejemplo: `1-16-11-01-01-31-04-003-018`
   - Reemplaza el identificador arbitrario por una clave jerárquica con referencia espacial atómica.
2. **Capacidad Operativa de Ruta**:
   - Capacidad objetivo: **180 suministros** con tolerancia de **±20** (rango operativo: **160 a 200 suministros** por ruta).
3. **Algoritmo de Bin-Packing Espacial por Manzana Atómica Colindante**:
   - Agrupación indivisible a nivel manzana catastral (`DD-PP-LL-CC-SS-MMM` / 13 dígitos).
   - Barrido espacial (Spatial Sweep) por proximidad de centroides `(latitud, longitud)` dentro del mismo `distrito` y `grupo_lectura`.
   - Tratamiento de macro-manzanas (>200 suministros): partición interna secuencial por parcelas/lotes sin cruzar límites barriales.

## 📊 Resultados del Piloto (Distrito 1 - Grupo de Lectura 16)
- **Suministros Totales Procesados**: 47.794 suministros activos.
- **Localidades Involucradas**: Córdoba Capital (42.310 sum.), Malagueño (5.137 sum. - 97,4% de la localidad), Yoccina (452 sum. - 97,2% de la localidad), Villa San Nicolás (1 sum.).
- **Manzanas Catastrales Únicas**: 2.529 manzanas.
- **Rutas Anteriores (SIGEC)**: 122 rutas heterogéneas (media: 391,8 suministros).
- **Nuevas Rutas Generadas**: **286 rutas homogéneas** (`16001` a `16286`).
- **Media de Suministros por Ruta**: **167,1 suministros** (Mediana: 168).
- **Cumplimiento en Rango [160, 200]**: **82,2%**.

## 💾 Entregables
- Script de procesamiento: `scripts/generar_nuevas_rutas_g16.py`
- Padrón individual: `C:\Users\jidiaz\Downloads\propuesta_nuevas_rutas_distrito1_grupo16.csv`
- Resumen de rutas: `C:\Users\jidiaz\Downloads\resumen_rutas_propuestas_g16.csv`
- Informe técnico de propuesta: `propuesta_nuevas_rutas_distrito1_grupo16.md`
