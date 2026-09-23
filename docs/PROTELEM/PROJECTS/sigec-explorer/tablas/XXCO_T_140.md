---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 1000
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_T_140"
---

# 🔧 XXCO_T_140

**Filas estimadas:** 1,000

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PERIODOS_2019` | NUMBER | YES |  |  |
| `CONS_012019` | NUMBER | YES |  |  |
| `DIAS_012019` | NUMBER | YES |  |  |
| `CONS_DIA_012019` | NUMBER | YES |  |  |
| `CONS_022019` | NUMBER | YES |  |  |
| `DIAS_022019` | NUMBER | YES |  |  |
| `CONS_DIA_022019` | NUMBER | YES |  |  |
| `CONS_032019` | NUMBER | YES |  |  |
| `DIAS_032019` | NUMBER | YES |  |  |
| `CONS_DIA_032019` | NUMBER | YES |  |  |
| `CONS_042019` | NUMBER | YES |  |  |
| `DIAS_042019` | NUMBER | YES |  |  |
| `CONS_DIA_042019` | NUMBER | YES |  |  |
| `CONS_052019` | NUMBER | YES |  |  |
| `DIAS_052019` | NUMBER | YES |  |  |
| `CONS_DIA_052019` | NUMBER | YES |  |  |
| `CONS_062019` | NUMBER | YES |  |  |
| `DIAS_062019` | NUMBER | YES |  |  |
| `CONS_DIA_062019` | NUMBER | YES |  |  |
| `CONS_072019` | NUMBER | YES |  |  |
| `DIAS_072019` | NUMBER | YES |  |  |
| `CONS_DIA_072019` | NUMBER | YES |  |  |
| `CONS_082019` | NUMBER | YES |  |  |
| `DIAS_082019` | NUMBER | YES |  |  |
| `CONS_DIA_082019` | NUMBER | YES |  |  |
| `CONS_092019` | NUMBER | YES |  |  |
| `DIAS_092019` | NUMBER | YES |  |  |
| `CONS_DIA_092019` | NUMBER | YES |  |  |
| `CONS_102019` | NUMBER | YES |  |  |
| `DIAS_102019` | NUMBER | YES |  |  |
| `CONS_DIA_102019` | NUMBER | YES |  |  |
| `CONS_112019` | NUMBER | YES |  |  |
| `DIAS_112019` | NUMBER | YES |  |  |
| `CONS_DIA_112019` | NUMBER | YES |  |  |
| `CONS_122019` | NUMBER | YES |  |  |
| `DIAS_122019` | NUMBER | YES |  |  |
| `CONS_DIA_122019` | NUMBER | YES |  |  |
| `CONS_012020` | NUMBER | YES |  |  |
| `DIAS_012020` | NUMBER | YES |  |  |
| `CONS_DIA_012020` | NUMBER | YES |  |  |
| `CONS_022020` | NUMBER | YES |  |  |
| `DIAS_022020` | NUMBER | YES |  |  |
| `CONS_DIA_022020` | NUMBER | YES |  |  |
| `CONS_032020` | NUMBER | YES |  |  |
| `DIAS_032020` | NUMBER | YES |  |  |
| `CONS_DIA_032020` | NUMBER | YES |  |  |
