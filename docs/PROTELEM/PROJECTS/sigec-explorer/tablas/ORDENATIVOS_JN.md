---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 116888627
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "ORDENATIVOS_JN"
---

# 📝 ORDENATIVOS_JN

**Filas estimadas:** 116,888,627

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | YES |  |
| `ORD_NUMERO` | NUMBER | YES |  |
| `ORD_FECHA_INICIO` | DATE | YES |  |
| `ORD_FECHA_VENCIMIENTO` | DATE | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USUARIO` | VARCHAR2 | YES |  |
| `JN_USUARIO_AUT` | VARCHAR2 | YES |  |
| `JN_USR_SITUACION` | VARCHAR2 | YES |  |
| `JN_USR_IMPRIMIO` | VARCHAR2 | YES |  |
| `JN_OLD_SITUACION` | VARCHAR2 | YES |  |
| `TRT_NUMERO` | NUMBER | YES |  |
| `JN_ORD_OBSERVA` | VARCHAR2 | YES |  |
| `LOR_NUMERO` | NUMBER | YES |  |
| `JN_LOR_NUMERO_PADRE` | NUMBER | YES |  |
| `JN_ORD_RESULTADO` | VARCHAR2 | YES |  |
| `JN_NEW_SITUACION` | VARCHAR2 | YES |  |
| `JN_NEW_LOR_NUMERO_PADRE` | NUMBER | YES |  |
| `JN_NEW_LOR_NUMERO` | NUMBER | YES |  |
| `JN_OLD_ESTADO` | VARCHAR2 | YES |  |
| `JN_OLD_SEC_CODIGO_DESTINO` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `LOR_NUMERO` → [[XXCO_LOTE_ORDENATIVOS_MOV]] _LOR_NUMERO es PK de XXCO_LOTE_ORDENATIVOS_MOV_
