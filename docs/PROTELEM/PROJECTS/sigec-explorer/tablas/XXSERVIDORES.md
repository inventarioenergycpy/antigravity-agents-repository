---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 15
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XXSERVIDORES"
---

# 📋 XXSERVIDORES

**Filas estimadas:** 15

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SER_NOMBRE` | VARCHAR2 | NO | 🔑 PK |
| `SER_DESCRIPCION` | VARCHAR2 | YES |  |
| `SER_USUARIO` | VARCHAR2 | YES |  |
| `SER_PASSWORD` | VARCHAR2 | YES |  |
| `SER_PRIMARIO` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XXTIPOS_TRANSFER_ARCHIVOS]] via `SER_NOMBRE_DESTINO`, `SER_NOMBRE_ORIGEN`
