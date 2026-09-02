---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 40
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "EQUIVALENCIAS"
---

# 📋 EQUIVALENCIAS

**Filas estimadas:** 40

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `EQUI_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `EQUI_ORIGEN` | VARCHAR2 | NO | 🔑 PK |
| `EQUI_DESTINO` | VARCHAR2 | NO | 🔑 PK |
| `EQUI_CODIGO_ORIGEN` | VARCHAR2 | NO | 🔑 PK |
| `EQUI_CODIGO_DESTINO` | VARCHAR2 | NO | 🔑 PK |
| `EQUI_DESCRIPCION` | VARCHAR2 | YES |  |
| `EQUI_FECHA_DESDE` | DATE | NO |  |
| `EQUI_FECHA_HASTA` | DATE | YES |  |
