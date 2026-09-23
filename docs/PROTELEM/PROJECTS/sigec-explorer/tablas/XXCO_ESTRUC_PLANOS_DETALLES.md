---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: equipos
num_rows: 1137
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/equipos
aliases:
  - "XXCO_ESTRUC_PLANOS_DETALLES"
---

# 🔧 XXCO_ESTRUC_PLANOS_DETALLES

**Filas estimadas:** 1,137

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `EPD_SECUENCIA` | NUMBER | NO | 🔑 PK |
| `EPD_COLUMNA` | VARCHAR2 | YES |  |
| `EPD_VARIABLE` | VARCHAR2 | YES |  |
| `EPD_TAMANIO` | NUMBER | YES |  |
| `EPD_PAD` | VARCHAR2 | YES |  |
| `EPD_LR_PAD` | VARCHAR2 | YES |  |
| `EPT_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `EPD_REPETIBLE` | VARCHAR2 | YES |  |
| `EPD_CAN_REPETIBLE` | NUMBER | YES |  |
| `EPD_TIPO_VARIABLE` | VARCHAR2 | YES |  |
| `EPD_MASCARA` | VARCHAR2 | YES |  |
| `EPD_RELACION_1` | VARCHAR2 | YES |  |
| `EPD_RELACION_2` | VARCHAR2 | YES |  |
| `EPD_RELACION_3` | VARCHAR2 | YES |  |
| `EPD_RELACION_4` | VARCHAR2 | YES |  |
| `EPD_RELACION_5` | VARCHAR2 | YES |  |
| `EPD_RELACION_6` | VARCHAR2 | YES |  |
| `EPD_RELACION_7` | VARCHAR2 | YES |  |
| `EPD_COLUMNA_XML` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XXCO_ESTRUC_PLANOS_GRP_REP]] via `EPD_SECUENCIA`, `EPT_TIPO`
