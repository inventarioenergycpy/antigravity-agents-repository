---
type: proyecto
proyecto: "Control de Rutas de Lecturas - Nuevas Rutas (Power BI PBIP)"
agente_responsable: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
ubicacion_red: "\\srvfs01\ProyectoTelemedicion\SQL\4_Power_BI_listos\Control de rutas de lecturas - Nuevas Rutas - proyecto.pbip"
fecha_creacion: 2026-09-03
fecha_actualizacion: 2026-09-04
tags:
  - #proyecto
  - #powerbi
  - #pbip
  - #tmdl
  - #modelo-estrella
  - #catastro
  - #ruteo-lectura
  - #epec
---

# 📊 Proyecto: Control de Rutas de Lecturas - Nuevas Rutas (Power BI PBIP)

- **Archivo PBIP**: `\\srvfs01\ProyectoTelemedicion\SQL\4_Power_BI_listos\Control de rutas de lecturas - Nuevas Rutas - proyecto.pbip`
- **Agente Responsable**: `[[docs/Agentes/02-Ciencia-de-Datos|02 - Ciencia de Datos & Ingeniero de Analytics BI]]`

---

## 🎯 Objetivos y Alcance de la Transformación

1. **Modelado Dimensional en Estrella (Star Schema)**:
   - Descomposición de la tabla `GEOREF_VM_SUMINISTROS` en un modelo estrella en **Power Query (Lenguaje M)** con claves subrogadas enteras (`Int64`), reduciendo más del 65% de memoria.
   - **Dimensiones Activas Creadas**:
     * `Dim_Red_Electrica` (exclusivamente con `DISTRIBUIDOR`, `SUBESTACION`, `SEA` - *sin PCT ni ORIGEN*).
     * `Dim_Tarifa` (`GRUPO_TARIFARIO`, `CODIGO_TARIFA`, `TARIFA`, `CLASE`, `DESCRIPCION_CLASE`, `TENSION`).
     * `Dim_Geografia` (`BAR_CODIGO`, `BARRIO`, `BARRIO_GEOREF`, `LOCALIDAD`, `AGF_CODIGO`, `CP`).
     * `Dim_Medidor` (`MEDIDOR_MARCA`, `MEDIDOR_FASES`, `GRUPO_FASES_MEDIDOR`, `TELEMEDIBLE`, `SENSIBILIDAD`).
     * `Dim_Ruta_Actual` (`DISTRITO`, `DISTRITO_DESCRIPCION`, `GRUPO_LECTURA`, `RUTA_LECTURA`).
     * `Dim_Estado_Servicio` (`ESTADO_SERVICIO`, `ESTADO_CONTRATO`, `TIPO_CLIENTE`, `FACTURA_DIGITAL`, `ESTADO_RELEVAMIENTO`).
   - **Atributos Catastrales en Fact Table**: Conservación directa de `DESCRIPCION_MANZANAS_CATASTRAL`, `DISTRITO_CATASTRAL`, `ZONA_CATASTRAL`, `MANZANA_CATASTRAL`, `LOTE_CATASTRAL`, `PH_CATASTRAL`, `ORIGEN_DC`, `DC`, `PCT`, `ORIGEN`, `DISTRITO` y `GRUPO_LECTURA` en `GEOREF_VM_SUMINISTROS`.

2. **Reorganización Algorítmica de Rutas (`TABLA_RUTAS_NUEVAS`)**:
   - **Agrupación Directa**: Agrupación por `DISTRITO`, `GRUPO_LECTURA` y `DESCRIPCION_MANZANAS_CATASTRAL` (clave de manzana de 13 dígitos derivada de la nomenclatura oficial `DC` de 16 dígitos).
   - **Cobertura 100%**: Condición `CANT_SUMI >= 1` erradicando casos huérfanos.
   - **Bin Packing de Rutas**: Asignación secuencial de `ID_RUTA_NUEVA` por manzana atómica dentro de cada par `(DISTRITO, GRUPO_LECTURA)` con límite de hasta **180 suministros por ruta**.

---

## 🔗 Arquitectura de Relaciones (relationships.tmdl)

* `Dim_Red_Electrica[ID_RED_KEY]` ➡️ `GEOREF_VM_SUMINISTROS[ID_RED_KEY]` (1:N, Single)
* `Dim_Tarifa[ID_TARIFA_KEY]` ➡️ `GEOREF_VM_SUMINISTROS[ID_TARIFA_KEY]` (1:N, Single)
* `Dim_Geografia[ID_GEOGRAFIA_KEY]` ➡️ `GEOREF_VM_SUMINISTROS[ID_GEOGRAFIA_KEY]` (1:N, Single)
* `Dim_Medidor[ID_MEDIDOR_KEY]` ➡️ `GEOREF_VM_SUMINISTROS[ID_MEDIDOR_KEY]` (1:N, Single)
* `Dim_Ruta_Actual[ID_RUTA_ACTUAL_KEY]` ➡️ `GEOREF_VM_SUMINISTROS[ID_RUTA_ACTUAL_KEY]` (1:N, Single)
* `Dim_Estado_Servicio[ID_ESTADO_KEY]` ➡️ `GEOREF_VM_SUMINISTROS[ID_ESTADO_KEY]` (1:N, Single)
* `relevamiento_castastral[REL_SUMINISTRO]` ➡️ `GEOREF_VM_SUMINISTROS[SUMINISTRO]` (1:N, Single)
* `GEOREF_VM_SUMINISTROS[DESCRIPCION_MANZANAS_CATASTRAL]` ➡️ `TABLA_RUTAS_NUEVAS[DESCRIPCION_MANZANAS_CATASTRAL]` (N:M / 1:N)

---

## 🛠️ Historial de Incidentes y Resoluciones TMDL

Para el detalle exhaustivo de diagnósticos y soluciones aplicadas, consultar:  
👉 **[[docs/Historial-Mejoras/2026-09-04_ciencia-de-datos_historial-fallas-y-soluciones-tmdl-pbip|Historial de Fallas y Soluciones TMDL / PBIP]]**  
👉 **[[docs/Historial-Mejoras/2026-09-06_ciencia-de-datos_resolucion-fallas-pbip-json-schema-y-artefactos|Resolución de Fallas PBIP JSON Schema y Artefactos (Power BI Release 2026)]]**

1. **Incidente UTF-8 BOM (2026-09-03)**: Resuelto mediante eliminación del preámbulo BOM en `.tmdl`.
2. **Incidente Jerarquía de Fechas (2026-09-03)**: Resuelto armonizando tilde en `'Jerarquía de fechas'`.
3. **Incidente Doble UTF-8 / Mojibake (2026-09-04)**: Resuelto corrigiendo bytes de `Variación` (`0xC3 0xB3`) y limpiando comentarios en M.
4. **Incidente $schema JSON & PBIP Artifacts (2026-09-06)**: Resuelto ajustando URLs de esquema canónicas de Fabric 2026, vinculación `.Dataset\definition.pbi-dataset` y reescritura estricta de la clave `"$schema"`.

---

## 🚀 Escalamiento Algorítmico al Distrito 1 Completo (2026-10-14)

- **Universo Procesado**: **585.472 suministros** correspondientes a los 20 grupos cíclicos regulares de lectura del Distrito 1.
- **Rutas Históricas Reemplazadas**: 1.941 rutas anteriores con alta dispersión y desbalance (10 a >1.000 suministros).
- **Nuevas Rutas Creadas**: **3.669 rutas homogéneas** numeradas jerárquicamente por grupo (`01001` a `20253`).
- **Media Global**: **159,6 suministros/ruta** (Mediana global: 167 suministros/ruta).
- **Nuevo Identificador Catastral**: `1-{GRUPO}-{MANZANA_WFS}-{PARCELA}` asignado al 100% de los suministros con trazabilidad cartográfica WFS.

---

## 🌟 Evolución Topológica: Ruteo Conexo con Maximización de Calles Internas Compartidas (2026-10-23)

- **Problema Corregido**: Se erradicó la fragmentación y falta de contigüidad espacial del barrido 1D anterior, integrando el grafo de calles perimetrales de la capa oficial WFS (`EPEC:vm_manzanas_calles_new`) y las direcciones de suministros en SIGEC.
- **Universo Consolidado**: **585.727 suministros** asignados al 100% (0 cuentas huérfanas).
- **Rutas Conexas Generadas**: **3.300 rutas homogéneas compactas**.
- **Media Global**: **177,4 suministros/ruta** (altamente balanceadas en torno al target óptimo de 180).
- **Calles Internas Compartidas**: Promedio de **10,16 calles compartidas por ruta** en rutas multi-manzana, garantizando que el tomador de estado recorra ambas aceras de forma continua.
- **Código de Trazabilidad Catastral Enriquecido (`CTC-GEO`)**:
  `1-{GRUPO}-{DPPO}-{PED}-{PUEB}-{CIRC}-{SECC}-{MZA}-{PARC}-{GEO_QUAD}`
  con columnas explícitas de centroide lat/lon, cuadrante espacial (`GEO_QUAD`), calles perimetrales, listado y conteo de calles compartidas en ruta, y orden secuencial peatonal (`orden_lectura_sugerido`).
- **Entregables Actualizados**:
  * Padrón general: `C:\Users\jidiaz\Downloads\padron_nuevas_rutas_distrito1_completo.csv` (105,4 MB, 585.727 filas).
  * Padrón Parquet: `D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\padron_nuevas_rutas_distrito1_completo.parquet` (32,8 MB).
  * Matriz de rutas: `D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\resumen_todas_rutas_nuevas_distrito1.csv` (3.300 rutas).
  * Resumen de grupos: `D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\resumen_comparativo_grupos_distrito1.csv`.
  * Script en producción: `D:\Proyectos\sigec-ruta-nueva-catastro-georef\scripts\escalar_nuevas_rutas_distrito1.py`.


