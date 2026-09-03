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
   - DescomposiciÃ³n de la tabla ancha y monolÃ­tica `GEOREF_VM_SUMINISTROS` (66 columnas) en un modelo estrella en **Power Query (Lenguaje M)** con claves subrogadas enteras (`Int64`), reduciendo la redundancia de texto en mÃ¡s del 65% y maximizando la compresiÃ³n columnar VertiPaq.
   - **Dimensiones Creadas**:
     * `Dim_Red_Electrica` (exclusivamente con `DISTRIBUIDOR`, `SUBESTACION`, `SEA`).
     * `Dim_Tarifa` (`GRUPO_TARIFARIO`, `CODIGO_TARIFA`, `TARIFA`, `CLASE`, `DESCRIPCION_CLASE`, `TENSION`).
     * `Dim_Geografia` (`BAR_CODIGO`, `BARRIO`, `BARRIO_GEOREF`, `LOCALIDAD`, `AGF_CODIGO`, `CP`).
     * `Dim_Medidor` (`MEDIDOR_MARCA`, `MEDIDOR_FASES`, `GRUPO_FASES_MEDIDOR`, `TELEMEDIBLE`, `SENSIBILIDAD`).
     * `Dim_Catastro_Manzana` (`DESCRIPCION_MANZANAS_CATASTRAL`, `DISTRITO_CATASTRAL`, `ZONA_CATASTRAL`, `MANZANA_CATASTRAL`, `ORIGEN_DC`).
     * `Dim_Ruta_Actual` (`DISTRITO`, `DISTRITO_DESCRIPCION`, `GRUPO_LECTURA`, `RUTA_LECTURA`).
     * `Dim_Estado_Servicio` (`ESTADO_SERVICIO`, `ESTADO_CONTRATO`, `TIPO_CLIENTE`, `FACTURA_DIGITAL`, `ESTADO_RELEVAMIENTO`).

2. **ReorganizaciÃ³n AlgorÃ­tmica de Rutas (`TABLA_RUTAS_NUEVAS`)**:
   - **Nomenclatura Catastral Oficial (16 dÃ­gitos)**:
     - Departamento: 2 dÃ­gitos
     - PedanÃ­a: 2 dÃ­gitos
     - Pueblo / Localidad: 2 dÃ­gitos
     - CircunscripciÃ³n: 2 dÃ­gitos
     - SecciÃ³n: 2 dÃ­gitos
     - Manzana: 3 dÃ­gitos
     - Parcela / Lote: 3 dÃ­gitos
   - **Clave de Manzana**: `LEFT(DC, LEN(DC) - 3)` agrupando todos los suministros de la misma manzana fÃ­sica.
   - **Cobertura 100%**: EliminaciÃ³n del filtro excluyente `CANT_SUMI >= 3` (ahora `CANT_SUMI >= 1`) para evitar suministros huÃ©rfanos.
   - **Bin Packing de Rutas**: AsignaciÃ³n secuencial de `ID_RUTA_NUEVA` por manzana atÃ³mica dentro de cada `GRUPO_LECTURA` con lÃ­mite Ã³ptimo de hasta **180 suministros por ruta**.

---

## ðŸ“ Arquitectura de Relaciones (relationships.tmdl)

* `Dim_Red_Electrica[ID_RED_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_RED_KEY]` (1:N, Single)
* `Dim_Tarifa[ID_TARIFA_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_TARIFA_KEY]` (1:N, Single)
* `Dim_Geografia[ID_GEOGRAFIA_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_GEOGRAFIA_KEY]` (1:N, Single)
* `Dim_Medidor[ID_MEDIDOR_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_MEDIDOR_KEY]` (1:N, Single)
* `Dim_Catastro_Manzana[ID_MANZANA_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_MANZANA_KEY]` (1:N, Single)
* `Dim_Ruta_Actual[ID_RUTA_ACTUAL_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_RUTA_ACTUAL_KEY]` (1:N, Single)
* `Dim_Estado_Servicio[ID_ESTADO_KEY]` âž” `GEOREF_VM_SUMINISTROS[ID_ESTADO_KEY]` (1:N, Single)
* `Dim_Catastro_Manzana[DESCRIPCION_MANZANAS_CATASTRAL]` âž” `TABLA_RUTAS_NUEVAS[DESCRIPCION_MANZANAS_CATASTRAL]` (1:N, Single)
