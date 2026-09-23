---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2280423
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ASIENTOS_CONTABLES"
---

# 📋 ASIENTOS_CONTABLES

**Filas estimadas:** 2,280,423

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ASI_NUMERO` | NUMBER | NO | 🔑 PK |
| `ASI_FECHA` | DATE | NO |  |
| `ASI_FECHA_GENERACION` | DATE | NO |  |
| `URC_CODIGO` | NUMBER | YES | 🔗 → [[UNIDADES_RECAUDADORAS]] |
| `ASI_PROCESO` | VARCHAR2 | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `ASI_SUBDIARIO` | NUMBER | YES |  |
| `ASI_AUXILIAR` | NUMBER | YES |  |
| `ASI_COMENTARIO` | VARCHAR2 | YES |  |
| `ASI_ESTADO` | VARCHAR2 | YES |  |
| `USR_NUMERO_AUTORIZACION` | NUMBER | YES | 🔗 → [[USUARIOS]] |
| `CPR_NUMERO_INFORME_GL` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **ASI_AUTORIZADO_POR**: `USR_NUMERO_AUTORIZACION` → [[USUARIOS]] (`USR_NUMERO`)
- **ASI_FK_URC**: `URC_CODIGO` → [[UNIDADES_RECAUDADORAS]] (`URC_CODIGO`)
