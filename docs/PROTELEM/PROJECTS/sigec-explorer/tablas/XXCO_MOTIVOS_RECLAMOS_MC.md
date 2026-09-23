---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 15
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_MOTIVOS_RECLAMOS_MC"
---

# 🔧 XXCO_MOTIVOS_RECLAMOS_MC

**Filas estimadas:** 15

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MRE_CODIGO` | VARCHAR2 | NO |  |  |
| `MRE_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `MRE_DIAS_MAX_RESOLUCION` | NUMBER | NO |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | YES |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `MRE_TIPO` | VARCHAR2 | NO |  |  |
| `MRE_OPCION_IVR` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_DESTINO_FORZADO` | NUMBER | YES |  |  |
