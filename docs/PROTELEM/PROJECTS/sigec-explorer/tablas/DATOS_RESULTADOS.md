---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1039593
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DATOS_RESULTADOS"
---

# 📋 DATOS_RESULTADOS

**Filas estimadas:** 1,039,593

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DRE_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `DRE_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `DRE_DEMANDA_VACIO` | NUMBER | YES |  |  |
| `DRE_FASE` | VARCHAR2 | YES |  |  |
| `DRE_NOMBRE_OCUPANTE` | VARCHAR2 | YES |  |  |
| `DRE_NRO_MEDIDOR_PROXIMO` | NUMBER | YES |  |  |
| `DRE_PORC_ERROR` | NUMBER | YES |  |  |
| `DRE_NRO_PRECINTO` | VARCHAR2 | YES |  |  |
| `DRE_NOMBRE_POLICIA` | VARCHAR2 | YES |  |  |
| `DRE_NOMBRE_DUENIO` | VARCHAR2 | YES |  |  |
| `DRE_CANT_DIAS_CONSUMO` | NUMBER | YES |  |  |
| `DRE_CONCEPTO_FRAUDE` | VARCHAR2 | YES |  |  |
| `DRE_CONSUMO_ESTIMADO` | NUMBER | YES |  |  |
| `DRE_DEMANDA_ESTIMADA` | NUMBER | YES |  |  |
| `DRE_DETALLE_ADICIONAL` | VARCHAR2 | YES |  |  |
| `DRE_FACTOR_CARGA` | NUMBER | YES |  |  |
| `DRE_FECHA_CONSTATACION` | DATE | YES |  |  |
| `DRE_TIPO_CALCULO` | VARCHAR2 | YES |  |  |
| `DRE_DEMANDA_PERDIDA` | NUMBER | YES |  |  |
| `DRE_ESTADO_MEDIDOR` | NUMBER | YES |  |  |
| `DRE_PUESTA_CERO` | NUMBER | YES |  |  |
| `RCL_NUMERO` | NUMBER | YES |  |  |
| `DRE_NOMBRE_ESCRIBANO` | VARCHAR2 | YES |  |  |
| `DRE_CANT_OCUPANTES` | NUMBER | YES |  |  |
| `DRE_NRO_ACTA_INSPECCION` | VARCHAR2 | YES |  |  |
| `DRE_PRESENCIA_CLIENTE` | VARCHAR2 | YES |  |  |
| `DRE_OBSERVACION_ACTA` | VARCHAR2 | YES |  |  |
| `DRE_CAPACIDAD_MEDIDOR` | VARCHAR2 | YES |  |  |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `DRE_LECTURA` | NUMBER | YES |  |  |
| `DRE_PRESION_INTERNA` | NUMBER | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `DRE_FACTURACION_FRAUDE` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `DRE_FECHA_CREA` | DATE | YES |  |  |
| `USR_NUMERO_MODIFICA` | NUMBER | YES |  |  |
| `DRE_FECHA_MODIFICA` | DATE | YES |  |  |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `DRE_SUMARIO` | VARCHAR2 | YES |  |  |
| `DRE_UJ` | VARCHAR2 | YES |  |  |
| `DRE_CHOFER` | VARCHAR2 | YES |  |  |
| `DRE_FOTO` | VARCHAR2 | YES |  |  |
| `DRE_CARGA` | NUMBER | YES |  |  |
| `DRE_FASE_R` | NUMBER | YES |  |  |
| `DRE_FASE_S` | NUMBER | YES |  |  |
| `DRE_FASE_T` | NUMBER | YES |  |  |
| `DRE_NEUTRO` | NUMBER | YES |  |  |
| `DRE_FECHA_DESDE` | DATE | YES |  |  |
| `DRE_FECHA_HASTA` | DATE | YES |  |  |
| `DRE_PERIODO` | NUMBER | YES |  |  |
| `DRE_PROM_REGISTRADO` | NUMBER | YES |  |  |
| `DRE_PROM_ESTIMADO` | NUMBER | YES |  |  |
| `DRE_ENERGIA_NO_REG` | NUMBER | YES |  |  |
| `DRE_ELECTRICISTA` | VARCHAR2 | YES |  |  |
| `DRE_INSPECTOR` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `DRE_ESTADO` | VARCHAR2 | YES |  |  |
| `DRE_FECHA_TRANSMISION` | DATE | YES |  |  |
| `DRE_HORA` | VARCHAR2 | YES |  |  |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `DRE_ACTIVIDAD1` | VARCHAR2 | YES |  |  |
| `DRE_ACTIVIDAD2` | VARCHAR2 | YES |  |  |
| `DRE_FORMULA_ESTIMACION` | VARCHAR2 | YES |  |  |
| `DRE_TIPO_DOC_OCUPANTE` | VARCHAR2 | YES |  |  |
| `DRE_DOCUMENTO_OCUPANTE` | NUMBER | YES |  |  |
| `DRE_ESTADO_PLAN_REG` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO_BAR` | VARCHAR2 | YES |  |  |
| `DRE_ID_VEHICULO` | NUMBER | YES |  |  |
| `DRE_DOMINIO_VEHI` | VARCHAR2 | YES |  |  |
| `DRE_ESCRIBANO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **DRE_FK_PRS**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
