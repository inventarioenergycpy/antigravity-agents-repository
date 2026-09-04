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

1. **Incidente UTF-8 BOM (2026-09-03)**: Resuelto mediante eliminación del preámbulo BOM en `.tmdl`.
2. **Incidente Jerarquía de Fechas (2026-09-03)**: Resuelto armonizando tilde en `'Jerarquía de fechas'`.
3. **Incidente Doble UTF-8 / Mojibake (2026-09-04)**: Resuelto corrigiendo bytes de `Variación` (`0xC3 0xB3`) y limpiando comentarios en M.
