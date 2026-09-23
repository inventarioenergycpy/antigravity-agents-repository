---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: cobranza
num_rows: 53
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/cobranza
aliases:
  - "XXTIPOS_CARGA_ARCHIVOS"
---

# 📋 XXTIPOS_CARGA_ARCHIVOS

**Filas estimadas:** 53

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TCA_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TCA_DESCRIPCION` | VARCHAR2 | YES |  |
| `TCA_PATH_ARCHIVO_DATOS` | VARCHAR2 | YES |  |
| `TCA_NOMBRE_ARCHIVO_TCL` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XXTIPOS_TRANSFER_ARCHIVOS]] via `TCA_CODIGO`
