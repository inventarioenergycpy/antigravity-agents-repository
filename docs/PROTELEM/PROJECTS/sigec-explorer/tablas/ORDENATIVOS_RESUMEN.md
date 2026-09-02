---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ORDENATIVOS_RESUMEN"
---

# 📋 ORDENATIVOS_RESUMEN

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `ORD_FECHA_GENERACION` | DATE | NO |  |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | NO |  |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO_DESTINO` | NUMBER | NO |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `ORD_FECHA_INICIO` | DATE | NO |  |  |
| `ORD_FECHA_VENCIMIENTO` | DATE | YES |  |  |
| `ORD_RESULTADO` | VARCHAR2 | YES |  |  |
| `ORD_FECHA_FIN` | DATE | YES |  |  |
| `ORD_FECHA_CARGA_RESULTADO` | DATE | YES |  |  |
| `ORD_SITUACION` | VARCHAR2 | NO |  |  |
| `ORD_ESTADO` | VARCHAR2 | NO |  |  |
| `ORD_FECHA_ANULA` | DATE | YES |  |  |
