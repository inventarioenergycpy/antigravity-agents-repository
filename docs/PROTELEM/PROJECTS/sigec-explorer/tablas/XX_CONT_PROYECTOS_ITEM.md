---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "XX_CONT_PROYECTOS_ITEM"
---

# 📋 XX_CONT_PROYECTOS_ITEM

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DCI_NUMERO` | NUMBER | NO | 🔑 PK |
| `CPY_NUMERO` | NUMBER | NO | 🔗 → [[XX_CONTRIBUCIONES_PROYECTOS]] |
| `CPI_CUOTA` | NUMBER | NO |  |
| `CPI_PERIODO` | NUMBER | NO |  |
| `CPI_SALDO_INICIAL` | NUMBER | YES |  |
| `CPI_CONTRIBUCION` | NUMBER | YES |  |
| `CPI_DEMANDA_PERIODO` | NUMBER | YES |  |
| `IAF_NUMERO` | NUMBER | YES | 🔗 → [[ITEMS_A_FACTURAR]] |
| `CPI_APROBADA` | VARCHAR2 | NO |  |
| `CPI_FECHA_APROBACION` | DATE | YES |  |
| `USR_NUMERO_APROBACION` | NUMBER | YES |  |
| `CPI_FECHA_CREACION` | DATE | NO |  |
| `CPI_OBS_APROBACION` | VARCHAR2 | YES |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **CPI_CPY_FK**: `CPY_NUMERO` → [[XX_CONTRIBUCIONES_PROYECTOS]] (`CPY_NUMERO`)
- **CPI_IAR_FK**: `IAF_NUMERO` → [[ITEMS_A_FACTURAR]] (`IAF_NUMERO`)

## Tablas que referencian esta tabla

- [[XX_DOCUMENTOS_CONTRIB]] via `DCI_NUMERO`

## FK inferidas (alta confianza)

- `CPY_NUMERO` → [[XX_CONTRIBUCIONES_PROYECTOS]] _CPY_NUMERO es PK de XX_CONTRIBUCIONES_PROYECTOS_
