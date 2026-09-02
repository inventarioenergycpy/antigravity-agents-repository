---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 21142
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "RED_DEVUELTOS_ERR"
---

# 📋 RED_DEVUELTOS_ERR

**Filas estimadas:** 21,142

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `RTI_TIPO` | VARCHAR2 | NO | 🔗 → [[RED_DEVUELTOS]] |  |
| `RDE_ARCHIVO_DEV` | VARCHAR2 | NO | 🔗 → [[RED_DEVUELTOS]] |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `RDR_IMPORTE_RED` | NUMBER | YES |  |  |
| `RDR_FECHA_PAGO` | DATE | YES |  |  |
| `RER_CODIGO` | NUMBER | YES |  |  |
| `RDE_FECHA_RED` | DATE | YES | 🔗 → [[RED_DEVUELTOS]] |  |

## FK declaradas → otras tablas

- **RED_DEVUELTOS_FK**: `RTI_TIPO`, `RDE_ARCHIVO_DEV`, `RDE_FECHA_RED` → [[RED_DEVUELTOS]] (`RTI_TIPO`, `RDE_ARCHIVO_DEV`, `RDE_FECHA_RED`)

## FK inferidas (alta confianza)

- `RDE_ARCHIVO_DEV` → [[RED_DEVUELTOS]] _RDE_ARCHIVO_DEV es PK de RED_DEVUELTOS_
- `RDE_FECHA_RED` → [[RED_DEVUELTOS]] _RDE_FECHA_RED es PK de RED_DEVUELTOS_
