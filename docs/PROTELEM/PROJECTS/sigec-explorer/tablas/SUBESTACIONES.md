---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1258
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "SUBESTACIONES"
---

# 📋 SUBESTACIONES

**Filas estimadas:** 1,258

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SUBEST` | VARCHAR2 | YES |  |
| `ZONA` | VARCHAR2 | YES |  |
| `SECTOR` | VARCHAR2 | YES |  |
| `FECHA` | DATE | YES |  |
| `TIPO_SET` | VARCHAR2 | YES |  |
| `MEDICION` | VARCHAR2 | YES |  |
| `PTNEUTRO` | NUMBER | YES |  |
| `PTDESCARGA` | NUMBER | YES |  |
| `POT_NOMINAL` | NUMBER | YES |  |
| `NRO_TRANSF` | VARCHAR2 | YES |  |
| `TIPO_FUSMT` | VARCHAR2 | YES |  |
| `DESCARGA` | VARCHAR2 | YES |  |
| `TIPO_FUSBT` | VARCHAR2 | YES |  |
| `SALEXCLUS` | NUMBER | YES |  |
| `SALSUBTERR` | NUMBER | YES |  |
| `NROCAJAJ24` | VARCHAR2 | YES |  |
| `ESTADOSET1` | VARCHAR2 | YES |  |
| `ESTADOSET2` | VARCHAR2 | YES |  |
| `ESTADOSET3` | VARCHAR2 | YES |  |
| `ESTADOSET4` | VARCHAR2 | YES |  |
| `ESTADOSET5` | VARCHAR2 | YES |  |
| `ESTADOSET6` | VARCHAR2 | YES |  |
| `ESTADOSET7` | VARCHAR2 | YES |  |
| `GRUPO` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
