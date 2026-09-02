---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 45890
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_CABECERA_PLAN"
---

# 📋 VKO_CABECERA_PLAN

**Filas estimadas:** 45,890

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO | 🔑 PK |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CAP_CUOTAS` | NUMBER | YES |  |  |
| `CAP_FECHA_CARGA` | DATE | YES |  |  |
| `CAP_ESTADO` | VARCHAR2 | YES |  |  |
| `CAP_FECHA_LIQUIDACION` | DATE | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `CAP_NRO_FINANCIACION` | NUMBER | YES |  |  |

## Tablas que referencian esta tabla

- [[VKO_DETALLE_DEUDA]] via `CAP_NRO_PLAN`
- [[VKO_PAGOS]] via `CAP_NRO_PLAN`
