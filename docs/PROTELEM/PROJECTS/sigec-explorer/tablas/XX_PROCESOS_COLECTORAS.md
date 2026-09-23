---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 141847
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_PROCESOS_COLECTORAS"
---

# 📋 XX_PROCESOS_COLECTORAS

**Filas estimadas:** 141,847

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCL_NUMERO` | NUMBER | NO | 🔑 PK |
| `GRL_CODIGO` | VARCHAR2 | NO |  |
| `CRL_ANIO` | NUMBER | NO |  |
| `CRL_PERIODO` | NUMBER | NO |  |
| `EPC_CODIGO` | VARCHAR2 | NO | 🔗 → [[XX_ESTADOS_PROCESO_COLECT]] |
| `USR_NUMERO` | NUMBER | NO | 🔗 → [[USUARIOS]] |
| `PCL_FECHA` | DATE | NO |  |
| `PCL_OBSERVACIONES` | VARCHAR2 | YES |  |
| `CLE_CODIGO` | VARCHAR2 | YES | 🔗 → [[XX_COLECTORAS]] |
| `USR_NUMERO_TOMA` | NUMBER | NO | 🔗 → [[USUARIOS]] |
| `TCO_CODIGO` | NUMBER | YES |  |
| `PCL_MODELO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **FK_PCL_CLE**: `CLE_CODIGO` → [[XX_COLECTORAS]] (`CLE_CODIGO`)
- **FK_PCL_EPC**: `EPC_CODIGO` → [[XX_ESTADOS_PROCESO_COLECT]] (`EPC_CODIGO`)
- **FK_PCL_USR_LANZA**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)
- **FK_PCL_USR_TOMA**: `USR_NUMERO_TOMA` → [[USUARIOS]] (`USR_NUMERO`)

## Tablas que referencian esta tabla

- [[XX_RUTAS_PROCESOS_COLECTORA]] via `PCL_NUMERO`

## FK inferidas (alta confianza)

- `USR_NUMERO_TOMA` → [[XXCO_ALTAS_COLECTOR]] _USR_NUMERO_TOMA es PK de XXCO_ALTAS_COLECTOR_
- `TCO_CODIGO` → [[XX_TIPOS_COLECTORAS]] _TCO_CODIGO es PK de XX_TIPOS_COLECTORAS_
- `EPC_CODIGO` → [[XX_ESTADOS_PROCESO_COLECT]] _EPC_CODIGO es PK de XX_ESTADOS_PROCESO_COLECT_
