---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 46877
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SERVICIOS_PE_DETALLE"
---

# 📋 SERVICIOS_PE_DETALLE

**Filas estimadas:** 46,877

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SPE_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[SERVICIOS_PE]] |  |
| `SPD_ORDEN` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SPD_RAZON_SOCIAL` | VARCHAR2 | YES |  |  |
| `SPD_DIRECCION` | VARCHAR2 | YES |  |  |
| `STE_NUMERO` | VARCHAR2 | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `SPD_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `SPD_CRUCE` | VARCHAR2 | YES |  |  |
| `SPD_DISTRITO` | NUMBER | YES |  |  |
| `SPD_ZONA` | NUMBER | YES |  |  |
| `SPD_MANZANA` | NUMBER | YES |  |  |
| `SPD_LOTE` | NUMBER | YES |  |  |
| `SPD_SUBESTACION` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **SPD_FK_SPE**: `SPE_CODIGO` → [[SERVICIOS_PE]] (`SPE_CODIGO`)
