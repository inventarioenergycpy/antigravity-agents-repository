---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 2038
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "ORDENATIVOS_EMITIDOS"
---

# 📋 ORDENATIVOS_EMITIDOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 2,038

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO |  |
| `SCF_CODIGO_DESTINO` | NUMBER | NO |  |
| `ANIO` | NUMBER | YES |  |
| `PERIODO` | NUMBER | YES |  |
| `CAN_EMI` | NUMBER | YES |  |
