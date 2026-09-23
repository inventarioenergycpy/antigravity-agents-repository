---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 96
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DIRECCIONES_MAIL"
---

# 📋 DIRECCIONES_MAIL

**Filas estimadas:** 96

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | YES | 🔗 → [[ZONAS]] |
| `SCF_CODIGO` | NUMBER | YES | 🔗 → [[SUCURSALES]] |
| `SMA_CODIGO` | VARCHAR2 | YES |  |
| `DMA_DIRECCION` | VARCHAR2 | YES |  |
| `DMA_FECHA_ALTA` | DATE | YES |  |
| `DMA_FECHA_BAJA` | DATE | YES |  |

## FK declaradas → otras tablas

- **SCF_FK**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)
- **ZON_FK**: `ZON_CODIGO` → [[ZONAS]] (`ZON_CODIGO`)

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `SMA_CODIGO` → [[SECTORES_MAIL]] _SMA_CODIGO es PK de SECTORES_MAIL_
