---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 214
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_COLECTORAS"
---

# 📋 XX_COLECTORAS

**Filas estimadas:** 214

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CLE_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CLE_DESCRIPCION` | VARCHAR2 | NO |  |
| `CLE_OBSERVACIONES` | VARCHAR2 | YES |  |
| `USR_NUMERO` | NUMBER | YES | 🔗 → [[USUARIOS]] |
| `TCO_CODIGO` | NUMBER | NO | 🔗 → [[XX_TIPOS_COLECTORAS]] |
| `SCF_CODIGO` | NUMBER | YES | 🔗 → [[SUCURSALES]] |
| `ECO_CODIGO` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **FK_CLE_SCF**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)
- **FK_CLE_TCO**: `TCO_CODIGO` → [[XX_TIPOS_COLECTORAS]] (`TCO_CODIGO`)
- **FK_CLE_USR**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)

## Tablas que referencian esta tabla

- [[XX_ASIGNACION_COLECTORAS]] via `CLE_CODIGO`
- [[XX_PROCESOS_COLECTORAS]] via `CLE_CODIGO`

## FK inferidas (alta confianza)

- `TCO_CODIGO` → [[XX_TIPOS_COLECTORAS]] _TCO_CODIGO es PK de XX_TIPOS_COLECTORAS_
