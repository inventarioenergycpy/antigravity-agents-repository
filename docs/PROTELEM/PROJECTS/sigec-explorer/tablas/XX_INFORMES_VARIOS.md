---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6242
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_INFORMES_VARIOS"
---

# 📋 XX_INFORMES_VARIOS

**Filas estimadas:** 6,242

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `INV_NUMERO` | NUMBER | NO | 🔑 PK |
| `TIV_CODIGO` | VARCHAR2 | NO |  |
| `IVR_FECHA_INFORME` | DATE | NO |  |
| `CPR_NUMERO` | NUMBER | NO |  |
| `ENE_VENDOR_ID` | NUMBER | NO | 🔗 → [[XX_ENTES_ESTATALES]] |
| `INV_FECHA_DESDE` | DATE | YES |  |
| `INV_FECHA_HASTA` | DATE | YES |  |
| `INV_OBSERVACIONES` | VARCHAR2 | YES |  |
| `INV_ESTADO` | VARCHAR2 | YES |  |
| `INV_INFORMADO_AP` | VARCHAR2 | YES |  |
| `INV_PENDIENTE_INFORMAR_AP` | VARCHAR2 | YES |  |
| `INV_FECHA_INFORMADO_AP` | DATE | YES |  |
| `INV_FECHA_PARCIAL` | DATE | YES |  |
| `INV_FECHA_RC` | DATE | YES |  |
| `INV_GENERADO_RC` | VARCHAR2 | YES |  |
| `INV_PENDIENTE_INFORMAR_RC` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **INV_ENE_FK**: `ENE_VENDOR_ID` → [[XX_ENTES_ESTATALES]] (`ENE_VENDOR_ID`)
