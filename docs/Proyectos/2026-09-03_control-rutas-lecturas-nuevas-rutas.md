---
type: proyecto
proyecto: "Control de Rutas de Lecturas - Nuevas Rutas (Power BI PBIP)"
agente_responsable: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
ubicacion_red: "\\srvfs01\ProyectoTelemedicion\SQL\4_Power_BI_listos\Control de rutas de lecturas - Nuevas Rutas - proyecto.pbip"
fecha_creacion: 2026-09-03
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

# ðŸ—ºï¸ Proyecto: Control de Rutas de Lecturas - Nuevas Rutas (Power BI PBIP)

- **Archivo PBIP**: `\\srvfs01\ProyectoTelemedicion\SQL\4_Power_BI_listos\Control de rutas de lecturas - Nuevas Rutas - proyecto.pbip`
- **Agente Responsable**: `[[docs/Agentes/02-Ciencia-de-Datos|02 - Ciencia de Datos & Ingeniero de Analytics BI]]`

---

## ðŸŽ¯ Objetivos y Alcance de la TransformaciÃ³n

1. **Modelado Dimensional en Estrella (Star Schema)**:
   - DescomposiciÃ³n de la tabla `GEOREF_VM_SUMINISTROS` en un modelo estrella en **Power Query (Lenguaje M)** con claves subrogadas enteras (`Int64`).
   - **Dimensiones Activas Creadas**:
     * `Dim_Red_Electrica` (exclusivamente con `DISTRIBUIDOR`, `SUBESTACION`, `SEA` - *sin PCT ni ORIGEN*).
     * `Dim_Tarifa` (`GRUPO_TARIFARIO`, `CODIGO_TARIFA`, `TARIFA`, `CLASE`, `DESCRIPCION_CLASE`, `TENSION`).
     * `Dim_Geografia` (`BAR_CODIGO`, `BARRIO`, `BARRIO_GEOREF`, `LOCALIDAD`, `AGF_CODIGO`, `CP`).
     * `Dim_Medidor` (`MEDIDOR_MARCA`, `MEDIDOR_FASES`, `GRUPO_FASES_MEDIDOR`, `TELEMEDIBLE`, `SENSIBILIDAD`).
     * `Dim_Ruta_Actual` (`DISTRITO`, `DISTRITO_DESCRIPCION`, `GRUPO_LECTURA`, `RUTA_LECTURA`).
     * `Dim_Estado_Servicio` (`ESTADO_SERVICIO`, `ESTADO_CONTRATO`, `TIPO_CLIENTE`, `FACTURA_DIGITAL`, `ESTADO_RELEVAMIENTO`).
   - **Atributos Catastrales en Fact Table**: La dimensiÃ³n catastral separada fue descartada por requerimiento, manteniendo `DESCRIPCION_MANZANAS_CATASTRAL`, `DISTRITO_CATASTRAL`, `ZONA_CATASTRAL`, `MANZANA_CATASTRAL`, `LOTE_CATASTRAL`, `PH_CATASTRAL`, `ORIGEN_DC`, `DC`, `PCT`, `ORIGEN`, `DISTRITO` y `GRUPO_LECTURA` directamente en `GEOREF_VM_SUMINISTROS`.

2. **ReorganizaciÃ³n AlgorÃ­tmica de Rutas (`TABLA_RUTAS_NUEVAS`)**:
   - **AgrupaciÃ³n Directa**: AgrupaciÃ³n por `DISTRITO`, `GRUPO_LECTURA` y `DESCRIPCION_MANZANAS_CATASTRAL` (clave de manzana de 13 dÃ­gitos derivada de la nomenclatura oficial `DC` de 16 dÃ­gitos).
   - **Cobertura 100%**: CondiciÃ³n `CANT_SUMI >= 1` erradicando casos huÃ©rfanos.
   - **Bin Packing de Rutas**: AsignaciÃ³n secuencial de `ID_RUTA_NUEVA` por manzana atÃ³mica dentro de cada par `(DISTRITO, GRUPO_LECTURA)` con lÃ­mite Ã³ptimo de hasta **180 suministros por ruta**.

---

## ðŸ“ Arquitectura de Relaciones (relationships.tmdl)

* `Dim_Red_Electrica[ID_RED_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_RED_KEY]` (1:N, Single)
* `Dim_Tarifa[ID_TARIFA_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_TARIFA_KEY]` (1:N, Single)
* `Dim_Geografia[ID_GEOGRAFIA_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_GEOGRAFIA_KEY]` (1:N, Single)
* `Dim_Medidor[ID_MEDIDOR_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_MEDIDOR_KEY]` (1:N, Single)
* `Dim_Ruta_Actual[ID_RUTA_ACTUAL_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_RUTA_ACTUAL_KEY]` (1:N, Single)
* `Dim_Estado_Servicio[ID_ESTADO_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_ESTADO_KEY]` (1:N, Single)
* `relevamiento_castastral[REL_SUMINISTRO]` âž” `GEOREF_VM_SUMINISTROS[SUMINISTRO]` (1:N, Single)
* `GEOREF_VM_SUMINISTROS[DESCRIPCION_MANZANAS_CATASTRAL]` âž” `TABLA_RUTAS_NUEVAS[DESCRIPCION_MANZANAS_CATASTRAL]` (N:M / 1:N)
